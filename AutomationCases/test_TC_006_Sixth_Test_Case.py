import pytest

import pytest


# to execute precondition method we need to pass fixture code method name in test case
# yield is used to execute the code after each test case
# Scope is used to execute the fixture at start and end of the module only
# Command to execute : pytest -v -s  .\test_TC_006_Sixth_Test_Case.py

@pytest.fixture(scope="module")
def fixture_code():
    print("this will execute before each test case")
    print("-----------------------------------------------")
    yield
    print("this will execute After each test case")
    print("-----------------------------------------------")


def test_tc_006_Test_Case_testing(fixture_code):
    print("this is Sanity test case code")


def test_tc_007_Test_Case_testing(fixture_code):
    print("this is Sanity test case code")
