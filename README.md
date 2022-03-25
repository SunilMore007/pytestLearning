# pytestLearning


API TESTING USING PYTHON

**User should have below libraries imported in the project**
1. import json
1. import pytest
1. import jsonpath
1. import requests

**info about command to execute the code**
-  Test case code must be written inside the method name must be started with test
-  to run test case command: pytest -s -v testcase/method name
-  To show print statement on console : -s
-  To show Test case status on console: -v
-  To Execute specific Test case : `-k file/method name`
-  To Execute specific tag Test case : -m Smoke  e.g.  `pytest -v -s -m Sanity AutomationCases`
- To Skip tagged Test case : `-m Smoke or tagnamepytest -v -s -m "not  TopPriority" AutomationCases`
- To Disable Warnings :`pytest -v -s --disable-pytest-warnings -m  "TopPriority" AutomationCases`
