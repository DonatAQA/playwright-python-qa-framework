from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from utils.config import Config


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def open(self):
        super().open(
            Config.UI_BASE_URL
        )

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_login_page_opened(self):
        expect(self.page).to_have_title("Swag Labs")
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.login_button).to_be_visible()

    def verify_error_message(self, text: str):
        expect(self.error_message).to_contain_text(text)