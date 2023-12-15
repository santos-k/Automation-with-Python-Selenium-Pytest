import unittest


class AppTesting(unittest.TestCase):

    def test_appsearch(self):
        # Your test logic here
        self.assertTrue(1 == 1, "Assertion failed: 1 is not equal to 1")
        print("1 equal to 1")

    def test_advanceSearch(self):
        # Your test logic here
        self.assertEqual(2 + 2, 4, "Assertion failed: 2 + 2 is not equal to 4")
        print("2+2 equals to 4")

    def test_gmail(self):
        print("3 not equals to 5")
        # Your test logic here
        self.assertNotEqual(3, 5, "Assertion failed: 3 is equal to 5")

    def test_assert_none(self):
        print("None value")
        value = None
        self.assertIsNone(value, "Assertion failed: Value is not None")

    def test_assert_not_none(self):
        print("Not none value")
        value = "Hello"
        self.assertIsNotNone(value, "Assertion failed: Value is None")

    def test_assert_in(self):
        print("3 in list")
        items = [1, 2, 3, 4, 5]
        self.assertIn(3, items, "Assertion failed: 3 is not in the list")

    def test_assert_not_in(self):
        print("6 is not in list")
        items = [1, 2, 3, 4, 5]
        self.assertNotIn(6, items, "Assertion failed: 6 is in the list")

    def test_relational_assert(self):
        print("5 is not less then 10")
        x = 5
        y = 10
        self.assertLess(x, y, "Assertion failed: {} is not less than {}".format(x, y))


if __name__ == "__main__":
    unittest.main()


<input id="input" class="truncate" type="search" autocomplete="off" placeholder="Search Google or type a URL">
