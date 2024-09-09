def assert_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code, \
        f"Expected status code {expected_status_code} but got {response.status_code}"

def assert_message(response, expected_message):
    assert response.json().get("message") == expected_message, \
        f"Expected message '{expected_message}' not found in response {response.json().get("message")}"
