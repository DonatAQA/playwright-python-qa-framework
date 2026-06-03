def assert_status_code(response, expected_status):
    assert response.status_code == expected_status, (
        f"Expected {expected_status}, "
        f"got {response.status_code}"
    )


def assert_response_key(body, key):
    assert key in body, (
        f"Missing key: {key}"
    )