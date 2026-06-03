import pytest
from data.users import STANDARD_USER, CUSTOMER_INFO

@pytest.mark.smoke
@pytest.mark.e2e
def test_complete_purchase_flow(
        login_page,
        products_page,
        cart_page,
        checkout_page
):
    login_page.open()
    login_page.login(STANDARD_USER["username"], STANDARD_USER["password"])

    products_page.verify_products_page_opened()
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.open_cart()

    cart_page.verify_cart_page_opened()
    cart_page.verify_product_in_cart("Sauce Labs Backpack")
    cart_page.proceed_to_checkout()

    checkout_page.verify_checkout_info_page_opened()

    checkout_page.fill_customer_info(
        CUSTOMER_INFO["first_name"],
        CUSTOMER_INFO["last_name"],
        CUSTOMER_INFO["postal_code"]
    )

    checkout_page.continue_checkout()
    checkout_page.finish_order()

    checkout_page.verify_order_completed()