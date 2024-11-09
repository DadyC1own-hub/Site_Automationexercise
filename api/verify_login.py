import requests


class VerifyLoginAPI:

    url = "https://automationexercise.com/api/verifyLogin"

    def verify_login(self, data):
        response = requests.post(self.url, data=data)
        return response
