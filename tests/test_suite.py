from playwright.sync_api import sync_playwright
import pytest


@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_chutney"),
        ("invalid_user", "secret_sauce"),
        ("", "secret_sauce"),
        ("standard_user", ""),
        ("", ""),
    ],
)
def test_invalid_login(username, password):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill(username)
        page.locator("#password").fill(password)
        page.locator("#login-button").click()

        assert page.get_by_text("Epic sadface:").is_visible()

        browser.close()


@pytest.mark.testCart
def test_adding_single_item_to_cart(page):
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator(".shopping_cart_link").click()
    assert page.get_by_text("Sauce Labs Backpack").is_visible()

@pytest.mark.testCart
def test_adding_multiple_items_to_cart(page):
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator("#add-to-cart-sauce-labs-fleece-jacket").click()
    page.locator("#add-to-cart-sauce-labs-onesie").click()
    page.locator(".shopping_cart_link").click()

    assert page.get_by_text("Sauce Labs Backpack").is_visible()
    assert page.get_by_text("Sauce Labs Onesie").is_visible()
    assert page.get_by_text("Sauce Labs Fleece Jacket").is_visible()

def test_successful_checkout(page):
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator("#add-to-cart-sauce-labs-fleece-jacket").click()
    page.locator("#add-to-cart-sauce-labs-onesie").click()
    page.locator(".shopping_cart_link").click()
    page.locator("#checkout").click()
    page.locator("#first-name").fill("Kaustubh")
    page.locator("#last-name").fill("Shekhar")
    page.locator("#postal-code").fill("101010")
    page.locator("#continue").click()
    page.locator("#finish").click()
    assert page.get_by_text("Thank you for your order!").is_visible()
