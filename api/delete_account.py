import requests

class DeleteAccountAPI:
    def __init__(self):
        self.url = "https://automationexercise.com/api/deleteAccount"

    def delete_account(self, data):
        response = requests.delete(self.url, data=data)
        return response
