# 1. setUp: execute before every test case (method)
# 2. tearDown: execute after every test case (method)
# 3. setUpClass: executes only once before test case start
# 4. tearDownClass: executes only once after test case start
# 5. setUpModule: executes before class executes
# 6. tearDownModule: execute after class executes

import unittest


def setUpModule():
    print("Set Up Module")


def tearDownModule():
    print("Tear Down Module")


class AppTesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Start Testing")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Testing Completed")

    def setUp(self) -> None:
        print("Login")

    def tearDown(self) -> None:
        print("Logout")

    def test_google(self):
        print("Actual test cases here")

    def test_gmail(self):
        print("This is Gmail test cases")


if __name__ == "__main__":
    unittest.main()
