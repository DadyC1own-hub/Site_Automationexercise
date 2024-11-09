from api.get_all_products import GetAllProductsAPI



class APIClientt:
    def __init__(self):
        self.get_all_products_api = GetAllProductsAPI()

    def get_all_products(self):
        return self.get_all_products_api.get_all_products()
