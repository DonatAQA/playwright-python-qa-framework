import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.ui
def test_saucedemo_login_page_opened(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.verify_login_page_opened()