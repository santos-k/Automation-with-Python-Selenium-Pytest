from PyTest.Sample_code.MyApp.sample import add


# testing add two num
def test_add_num():
    assert add(1, 2) == 3


# Testing add two string
def test_add_str():
    assert add("Py", "Test") == "PyTest"


class TestSample:

    # testing add two num
    def test_add_num(self):
        assert add(1, 2) == 3

    # Testing add two string
    def test_add_str(self):
        assert add("Py","Test") == "PyTest"


def testSample():
    assert add(2.4, 5) == 7.4


# Wrong test case
def test_add2():
    assert add(3, 7) == 11


def test_add3():
    assert add("Py", "Test") == "Pytest"


