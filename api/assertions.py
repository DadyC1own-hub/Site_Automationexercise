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



def assert_json_field(response, field, expected_value):

    actual_value = response.json().get(field)
    assert actual_value == expected_value, \
        f"Expected '{field}' to be '{expected_value}', but got '{actual_value}'"


def assert_response_time(response, max_time_ms):

    assert response.elapsed.total_seconds() * 1000 <= max_time_ms, \
        f"Response time exceeded {max_time_ms} ms. Actual time: {response.elapsed.total_seconds() * 1000:.2f} ms"


def assert_headers(response, expected_headers):

    for header, expected_value in expected_headers.items():
        actual_value = response.headers.get(header)
        assert actual_value == expected_value, \
            f"Expected header '{header}' to be '{expected_value}', but got '{actual_value}'"