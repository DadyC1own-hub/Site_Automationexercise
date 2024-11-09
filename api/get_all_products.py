import requests


class GetAllProductsAPI:

    url = "https://automationexercise.com/api/productsList"

    def get_all_products(self):
        response = requests.get(self.url)
        return response
