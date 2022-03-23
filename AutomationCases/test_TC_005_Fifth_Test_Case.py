import pytest

actual_result = "Testing"


def test_tc_005_Test_Case_testing():
    print("this is Sanity test case code")
    assert actual_result == "hello", "Two values must be same"
