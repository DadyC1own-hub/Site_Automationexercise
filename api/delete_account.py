import requests

class DeleteAccountAPI:

    url = "https://automationexercise.com/api/deleteAccount"

    def delete_account(self, data):
        response = requests.delete(self.url, data=data)
        return response
