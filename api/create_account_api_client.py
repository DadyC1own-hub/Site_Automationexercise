from api.create_account import CreateAccountAPI
from api.verify_login import VerifyLoginAPI
from api.delete_account import DeleteAccountAPI

class APIClient:
    def __init__(self):
        self.create_account_api = CreateAccountAPI()
        self.verify_login = VerifyLoginAPI()
        self.delete_account = DeleteAccountAPI()

    def create_account(self, data):
        return self.create_account_api.create_account(data)

    def verify_login(self, data):
        return self.verify_login.verify_login(data)

    def delete_account(self, data):
        return self.delete_account.delete_account(data)