import requests


class CreateAccountAPI:

    url = "https://automationexercise.com/api/createAccount"

    def create_account(self, data):
        response = requests.post(self.url, json=data)
        return response
