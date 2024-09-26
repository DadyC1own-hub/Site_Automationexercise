import pytest
from api.create_account_api_client import APIClient
from api.get_all_products_api_client import APIClientt

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def api_client_get_all_product():
    return APIClientt()