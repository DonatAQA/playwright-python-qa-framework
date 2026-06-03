import requests


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, endpoint: str):
        return requests.get(f"{self.base_url}{endpoint}")

    def post(self, endpoint: str, payload: dict):
        return requests.post(f"{self.base_url}{endpoint}", json=payload)

    def delete(self, endpoint: str):
        return requests.delete(f"{self.base_url}{endpoint}")