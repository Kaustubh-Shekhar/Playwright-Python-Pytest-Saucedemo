from pages.base_page import BasePage

class CheckoutPage(BasePage):
    INPUT_FIRST_NAME = "#first-name"
    INPUT_LAST_NAME = "#last-name"
    INPUT_ZIP_CODE = "#postal-code"
    BTN_CONTINUE = "#continue"
    BTN_FINISH = "#finish"
    FORM_INPUT = {"First Name": "Kaustubh", "Last Name": "Shekhar", "Zip Code": "101010"}

    def __init__(self, page):
        super().__init__(page)

    def fill_input(self, field, value):
        self.page.locator(field).fill(value)

    def fill_form(self):
        self.fill_input(self.INPUT_FIRST_NAME,self.FORM_INPUT["First Name"])
        self.fill_input(self.INPUT_LAST_NAME, self.FORM_INPUT["Last Name"])
        self.fill_input(self.INPUT_ZIP_CODE, self.FORM_INPUT["Zip Code"])

    def submit(self):
        self.page.locator(self.BTN_CONTINUE).click()

    def finish_checkout(self):
        self.page.locator(self.BTN_FINISH).click()