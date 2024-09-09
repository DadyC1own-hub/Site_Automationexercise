from dataModel.CreateAccount_models import CreateAccountRequest
from api.assertions import assert_status_code, assert_message


def test_create_account(api_client):
    # Создаем данные для запроса
    data = CreateAccountRequest.get_default().model_dump()

    # Отправка запроса и получение ответа
    response = api_client.create_account(data)

    # Используем функции для проверки статуса и сообщения
    assert_status_code(response, 201)
    # Знаю знаю но пока пускай будет
    assert_message(response, "User created!")
