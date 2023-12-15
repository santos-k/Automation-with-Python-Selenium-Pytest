import pytest

from PyTest.Assert_Exception.app.Assertion_app import validate_login


# valid test will pass
def test_validate_login_valid_test():
    validate_login("admin","admin123")


# invalid test will fail with error
def test_validate_login_invalid_test():
    validate_login("admin2", "admin123")


# checking that invalid test is invalid, so it will pass w/o error
def test_validate_login_invalid_test2():
    with pytest.raises(ValueError):
        validate_login("admin2", "admin123")


# invalid test is invalid, so it will pass with error info
def test_validate_login_invalid_test3():
    with pytest.raises(ValueError) as exc_info:
        validate_login("admin2", "admin123")
    print(str(exc_info.value))


# invalid test is invalid, match with expected error; pass
def test_validate_login_invalid_test4():
    with pytest.raises(ValueError) as exc_info:
        validate_login("admin2", "admin123")
    assert str(exc_info.value) == "Login denied, username or password maybe wrong."


# invalid test is invalid, match with unexpected error: fail
def test_validate_login_invalid_test5():
    with pytest.raises(ValueError) as exc_info:
        validate_login("admin2", "admin123")
    assert str(exc_info.value) == "Login success, username or password maybe wrong."


# invalid test is invalid, match with expected error: passa
def test_validate_login_invalid_test6():
    with pytest.raises(ValueError, match="Login denied, username or password maybe wrong."):
        validate_login("admin2", "admin123")
