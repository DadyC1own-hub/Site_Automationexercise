import allure

from data_models.create_account_models import CreateAccountRequest
from api.assertions_api import assert_status_code, assert_json_field

@allure.title("Создание аккаунта через API")
@allure.description("""
    Данный тест проверяет успешное создание аккаунта через API. 
    Проверяются статус ответа и наличие сообщения о создании пользователя.
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_account(api_client):
    # Создаем данные для запроса
    data = CreateAccountRequest.get_default().model_dump()

    # Шаг 1: Отправка запроса и получение ответа
    with allure.step("Отправка запроса на создание аккаунта"):
        response = api_client.create_account(data)

    # Шаг 2: Проверка статуса ответа
    with allure.step("Проверка статуса ответа"):
        assert_status_code(response, 201)

    # Шаг 3: Проверка содержимого ответа
    with allure.step("Проверка сообщения о создании пользователя"):
        assert_json_field(response, "User created!")
