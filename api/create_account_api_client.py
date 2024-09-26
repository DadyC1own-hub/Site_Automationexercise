from api.create_account_api import CreateAccountAPI


class APIClient:
    def __init__(self):
        self.create_account_api = CreateAccountAPI()

    def create_account(self, data):
        return self.create_account_api.create_account(data)
