from playwright.sync_api import sync_playwright
import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

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
def test_invalid_login(page,username,password):
    loginPage = LoginPage(page)
    loginPage.open()
    loginPage.login(username,password)
    assert page.get_by_text("Epic sadface:").is_visible()


@pytest.mark.testCart
def test_adding_single_item_to_cart(page):
    LoginPage(page).open()
    LoginPage(page).login()
    invPage = InventoryPage(page)
    invPage.add_backpack_to_cart()
    invPage.go_to_cart()
    assert page.get_by_text("Sauce Labs Backpack").is_visible()

@pytest.mark.testCart
def test_adding_multiple_items_to_cart(page):
    LoginPage(page).open()
    LoginPage(page).login()
    invPage = InventoryPage(page)
    invPage.add_backpack_to_cart()
    invPage.add_fleece_jacket_to_cart()
    invPage.add_onesie_to_cart()
    invPage.go_to_cart()

    assert page.get_by_text("Sauce Labs Backpack").is_visible()
    assert page.get_by_text("Sauce Labs Onesie").is_visible()
    assert page.get_by_text("Sauce Labs Fleece Jacket").is_visible()

def test_successful_checkout(page):
    LoginPage(page).open()
    LoginPage(page).login()

    invPage = InventoryPage(page)
    invPage.add_backpack_to_cart()
    invPage.add_fleece_jacket_to_cart()
    invPage.add_onesie_to_cart()
    invPage.go_to_cart()

    CartPage(page).initiate_checkout()
    checkoutPage = CheckoutPage(page)
    checkoutPage.fill_form()
    checkoutPage.submit()
    checkoutPage.finish_checkout()
    assert page.get_by_text("Thank you for your order!").is_visible()
