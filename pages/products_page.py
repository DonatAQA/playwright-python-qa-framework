from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.locator("[data-test='title']")
        self.inventory_items = page.locator("[data-test='inventory-item']")
        self.shopping_cart_link = page.locator("[data-test='shopping-cart-link']")

    def verify_products_page_opened(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(self.title).to_have_text("Products")
        expect(self.inventory_items).to_have_count(6)

    def add_product_to_cart(self, product_name: str):
        product = self.page.locator("[data-test='inventory-item']").filter(has_text=product_name)
        product.get_by_role("button", name="Add to cart").click()

    def open_cart(self):
        self.shopping_cart_link.click()