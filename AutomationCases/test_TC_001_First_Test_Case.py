import pytest


# Test case code must be written inside the method
# method name must be started with test
# to run test case command: pytest -s -v testcase/method name
# To show print statement on console : -s
# To show Test case status on console: -v
# To Execute specific Test case : -k file/method name
# To Execute specific tag Test case : -m Smoke or tagname  e.g.  pytest -v -s -m Sanity AutomationCases
# To Skip tagged Test case : -m Smoke or tagnamepytest -v -s -m "not  TopPriority" AutomationCases


@pytest.mark.Smoke
@pytest.mark.skip("skipping as this is not fully implemented ")
def test_tc_001_login_logout_testing():
    print("this is Smoke test case code")


a = 1


@pytest.mark.Sanity
@pytest.mark.skipif(a > 10, reason="Conditionally Skipped")
def test_tc_005_Invalid_login_logout_testing():
    print("this is Sanity  test case code")
