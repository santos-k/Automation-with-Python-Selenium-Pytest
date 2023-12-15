import sys

import pytest

from PyTest.Skip_Markers.app.app import validate_login


def test_validate_login_valid():
    validate_login("admin", "admin123")


# unconditional skip: without reason
@pytest.mark.skip
def test_skip():
    validate_login("user", "useradmin")


# skip with reason
# @pytest.mark.skip(reason="Just wanna skip it")
@pytest.mark.skip("Invalid Credentials")
def test_valid_login():
    validate_login("admin", "admin123")


# Conditional marker
@pytest.mark.skipif(sys.version_info > (3,8,1), reason="Python version 3.8.1 or older")
def test_valid_log2():
    validate_login("admin", "admin123")


# when you know it will throw an error, and you are ok with it
@pytest.mark.xfail
def test_validate_login2():
    validate_login("admin", "admin1234")


@pytest.mark.xfail(sys.platform == 'win32', reason="Runs only on windows")
def test_validate_login3():
    validate_login("admin", "admin12")


