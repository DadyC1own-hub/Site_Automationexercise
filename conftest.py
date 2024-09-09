import pytest
from api.api_client import APIClient
from api.API_client_get_all_products import APIClientt

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def api_client_get_all_product():
    return APIClientt()