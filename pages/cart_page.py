from pages.base_page import BasePage

class CartPage(BasePage):
    BTN_CHECKOUT = "#checkout"

    def __init__(self,page):
        super().__init__(page)

    def initiate_checkout(self):
        self.page.locator(self.BTN_CHECKOUT).click()