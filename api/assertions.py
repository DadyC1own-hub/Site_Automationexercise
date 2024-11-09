def assert_status_code(response, expected_code):
    # Проверяем, что HTTP статус ответа 200
    assert response.status_code == 200, \
        f"Expected status code {200} but got {response.status_code}"

    # Получаем реальный код из ответа
    response_data = response.json()  # Парсим тело ответа как JSON
    actual_code = response_data.get('responseCode')

    # Проверяем реальный код
    assert actual_code == expected_code, \
        f"Expected real code {expected_code} but got {actual_code}. Response: {response_data}"


def assert_message(response, expected_message):
    assert response.json().get("message") == expected_message, \
        f"Expected message '{expected_message}' not found in response '{response.json().get("message")}'"
