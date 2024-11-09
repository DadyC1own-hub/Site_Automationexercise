import allure
from dataModel.models import VerifyLoginRequest
from api.assertions import assert_status_code, assert_message

@allure.epic("User Management")
@allure.feature("Create Account")
@allure.story("Creating a new user account")
def test_delete_account(api_client):
    with allure.step("Создание данных для запроса"):
        data = VerifyLoginRequest.get_default().model_dump()

    with allure.step("Отправка запроса на удаление аккаунта"):
        response = api_client.delete_account.delete_account(data)

    with allure.step("Проверка кода статуса ответа"):
        assert_status_code(response, 200)

    with allure.step("Проверка сообщения ответа"):
        assert_message(response, "Account deleted!")
