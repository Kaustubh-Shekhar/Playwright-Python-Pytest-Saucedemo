from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self, username = "standard_user", password = "secret_sauce"):
            self.page.locator(self.USERNAME).fill(username)
            self.page.locator(self.PASSWORD).fill(password)
            self.page.locator(self.LOGIN_BTN).click()