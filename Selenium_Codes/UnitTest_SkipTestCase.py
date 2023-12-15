import unittest


class AppTesting(unittest.TestCase):

    @unittest.skip("Always skip")
    def test_appsearch(self):
        print("Test Search")

    @unittest.skip("Not ready for testing")
    def test_advanceSearch(self):
        print("Test advance search")

    @unittest.skipIf(1 == 1, "Condition True")
    def test_condition_true(self):
        print("Hello")

    @unittest.skipUnless(1 == 2, "Condition False")
    def test_condition_false(self):
        print("Hi")

    def test_gmail(self):
        print("This test case not skipped")


if __name__ == "__main__":
    unittest.main()
