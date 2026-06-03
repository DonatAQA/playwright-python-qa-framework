import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from data.users import STANDARD_USER


@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def products_page(page):
    return ProductsPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)

@pytest.fixture
def authenticated_user(login_page, products_page):
    login_page.open()

    login_page.login(
        STANDARD_USER["username"],
        STANDARD_USER["password"]
    )

    products_page.verify_products_page_opened()

    return products_page