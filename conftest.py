from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        yield page
        try:
            page.locator("#react-burger-menu-btn").click()
            page.locator("#logout_sidebar_link").click()
        except Exception:
            pass

        browser.close()