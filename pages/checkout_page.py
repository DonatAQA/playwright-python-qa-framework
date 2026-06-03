from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.locator("[data-test='title']")
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.complete_header = page.locator("[data-test='complete-header']")
        self.error_message = page.locator("[data-test='error']")

    def verify_checkout_info_page_opened(self):
        expect(self.title).to_have_text("Checkout: Your Information")

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()

    def verify_order_completed(self):
        expect(self.complete_header).to_have_text("Thank you for your order!")

    def verify_error_message(self, text: str):
        expect(self.error_message).to_contain_text(text)