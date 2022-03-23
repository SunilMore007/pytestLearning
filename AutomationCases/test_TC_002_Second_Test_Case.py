# Test case code must be written inside the method name must be started with test
# to run test case command: pytest testcase/method name
import pytest


@pytest.mark.Smoke
def test_tc_002_Registration_Testing():
    print("this is Smoke test case code")
