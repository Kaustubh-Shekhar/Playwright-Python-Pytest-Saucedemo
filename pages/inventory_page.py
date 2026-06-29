from pages.base_page import BasePage

class InventoryPage(BasePage):
    BTN_ADD_CART_BACKPACK = "#add-to-cart-sauce-labs-backpack"
    BTN_ADD_CART_FLEECE_JACKET = "#add-to-cart-sauce-labs-fleece-jacket"
    BTN_ADD_CART_ONESIE = "#add-to-cart-sauce-labs-onesie"
    CART_LINK = ".shopping_cart_link"

    def __init__(self,page):
        super().__init__(page)

    def add_backpack_to_cart(self):
        self.page.locator(self.BTN_ADD_CART_BACKPACK).click()

    def add_fleece_jacket_to_cart(self):
        self.page.locator(self.BTN_ADD_CART_FLEECE_JACKET).click()

    def add_onesie_to_cart(self):
        self.page.locator(self.BTN_ADD_CART_ONESIE).click()

    def go_to_cart(self):
        self.page.locator(self.CART_LINK).click()