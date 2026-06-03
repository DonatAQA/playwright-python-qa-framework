import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from data.users import STANDARD_USER


@pytest.mark.smoke
@pytest.mark.ui
def test_add_product_to_cart(
        authenticated_user,
        cart_page
):
    products_page = authenticated_user

    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.open_cart()

    cart_page.verify_cart_page_opened()
    cart_page.verify_product_in_cart("Sauce Labs Backpack")


@pytest.mark.regression
@pytest.mark.ui
def test_checkout_requires_first_name(
        authenticated_user,
        cart_page,
        checkout_page
):
    products_page = authenticated_user

    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.open_cart()

    cart_page.proceed_to_checkout()

    checkout_page.continue_checkout()
    checkout_page.verify_error_message("Error: First Name is required")