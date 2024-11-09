import requests


class VerifyLoginAPI:
    def __init__(self):
        self.url = "https://automationexercise.com/api/verifyLogin"

    def verify_login(self, data):
        response = requests.post(self.url, data=data)
        return response
