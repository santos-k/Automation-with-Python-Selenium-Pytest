from PyTest.Sample_code2.myapp.sample import validate_age


def test_vaidate_age_valid():
    validate_age(0)


def test_vaidate_age_valid2():
    validate_age(10)


def test_vaidate_age_valid3():
    validate_age(99)


def test_vaidate_age_invalid():
    validate_age(-1)


def test_vaidate_age_invalid2():
    validate_age(100)


def test_vaidate_age_invali3():
    validate_age(50.4)


def test_vaidate_age_invalid4():
    validate_age('four')

