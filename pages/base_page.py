from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def get_page_title(self):
        return self.page.title()

    def get_current_url(self):
        return self.page.url