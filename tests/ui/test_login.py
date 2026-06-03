import pytest

from data.users import STANDARD_USER, LOCKED_OUT_USER


@pytest.mark.smoke
@pytest.mark.ui
def test_successful_login(
        login_page,
        products_page
):
    login_page.open()

    login_page.login(
        STANDARD_USER["username"],
        STANDARD_USER["password"]
    )

    products_page.verify_products_page_opened()


@pytest.mark.regression
@pytest.mark.ui
def test_locked_out_user_login(
        login_page
):
    login_page.open()

    login_page.login(
        LOCKED_OUT_USER["username"],
        LOCKED_OUT_USER["password"]
    )

    login_page.verify_error_message(
        "Epic sadface: Sorry, this user has been locked out."
    )


@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.parametrize(
    "user_data, expected_result",
    [
        (STANDARD_USER, True),
        (LOCKED_OUT_USER, False)
    ]
)
def test_login_validation(
        login_page,
        products_page,
        user_data,
        expected_result
):
    login_page.open()

    login_page.login(
        user_data["username"],
        user_data["password"]
    )

    if expected_result:
        products_page.verify_products_page_opened()

    else:
        login_page.verify_error_message(
            "Epic sadface"
        )
