import pytest

# Test case code must be written inside the method
# method name must be started with test
# to run test case command: pytest -s -v testcase/method name
# To show print statement on console : -s
# To show Test case status on console: -v
# To Execute specific Test case : -k file/method name

@pytest.mark.skip("skipping as this is not fully implemented ")
def test_tc_001_login_logout_testing():
    print("this is our test case code")


a = 1


@pytest.mark.skipif(a > 10, reason="Conditionally Skipped")
def test_tc_003_Invalid_login_logout_testing():
    print("this is our test case code")
