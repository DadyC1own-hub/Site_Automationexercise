import allure
from dataModel.models import CreateAccountRequest
from api.assertions import assert_status_code, assert_message


@allure.epic("User Management")
@allure.feature("Create Account")
@allure.story("Creating a new user account")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_account(api_client):
    with allure.step("Создание данных для запроса"):
        data = CreateAccountRequest.get_default().model_dump()

    with allure.step("Отправка запроса на создание аккаунта"):
        response = api_client.create_account(data)

    with allure.step("Проверка кода статуса ответа"):
        assert_status_code(response, 201)

    with allure.step("Проверка сообщения ответа"):
        assert_message(response, "User created!")
