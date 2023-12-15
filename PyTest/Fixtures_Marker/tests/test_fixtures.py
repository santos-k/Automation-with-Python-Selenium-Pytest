# Fixtures
import json
import os
import pytest

from PyTest.Fixtures_Marker.app.sample import save_dict


# Define the tempdir fixture
@pytest.fixture
def tempdir(tmpdir):
    return tmpdir


def test_save_dict(tempdir, capsys):
    filepath = os.path.join(tempdir, "test.json")
    d = {'1': 'pytest', '2': 'python'}
    save_dict(d, filepath)
    assert json.load(open(filepath, 'r')) == d
    assert capsys.readouterr().out == "saved\n"
