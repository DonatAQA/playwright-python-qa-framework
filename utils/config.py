import os


class Config:

    UI_BASE_URL = os.getenv(
        "UI_BASE_URL",
        "https://www.saucedemo.com/"
    )

    API_BASE_URL = os.getenv(
        "API_BASE_URL",
        "https://jsonplaceholder.typicode.com"
    )