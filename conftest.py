from playwright.sync_api import sync_playwright
import pytest
import os


@pytest.fixture()
def page():
    with sync_playwright() as p:
        headless = os.getenv("CI") == "true"
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        yield page

        browser.close()