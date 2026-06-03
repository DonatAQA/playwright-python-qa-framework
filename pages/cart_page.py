from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.locator("[data-test='title']")
        self.cart_items = page.locator("[data-test='inventory-item']")
        self.checkout_button = page.locator("[data-test='checkout']")

    def verify_cart_page_opened(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")
        expect(self.title).to_have_text("Your Cart")

    def verify_product_in_cart(self, product_name: str):
        expect(self.cart_items.filter(has_text=product_name)).to_be_visible()

    def proceed_to_checkout(self):
        self.checkout_button.click()