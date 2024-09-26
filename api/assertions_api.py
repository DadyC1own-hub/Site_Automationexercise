
def assert_status_code(response, expected_status_code):

    assert response.status_code == expected_status_code, \
        f"Expected status code {expected_status_code}, but got {response.status_code}"


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
