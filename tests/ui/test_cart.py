import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from data.users import STANDARD_USER


@pytest.mark.smoke
@pytest.mark.ui
def test_add_product_to_cart(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.open()
    login_page.login(
        STANDARD_USER["username"],
        STANDARD_USER["password"]
    )

    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.open_cart()

    cart_page.verify_cart_page_opened()
    cart_page.verify_product_in_cart("Sauce Labs Backpack")


@pytest.mark.regression
@pytest.mark.ui
def test_checkout_requires_first_name(
        login_page,
        products_page,
        cart_page,
        checkout_page
):
    login_page.open()
    login_page.login(
        STANDARD_USER["username"],
        STANDARD_USER["password"]
    )

    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.open_cart()

    cart_page.proceed_to_checkout()

    checkout_page.continue_checkout()
    checkout_page.verify_error_message("Error: First Name is required")