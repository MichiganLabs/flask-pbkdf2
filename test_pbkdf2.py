#!/usr/bin/env python

import pytest

import flask
from flask_pbkdf2 import Pbkdf2

@pytest.fixture
def pbkdf2():
    app = flask.Flask(__name__)
    app.config['ITERATIONS'] = 1000
    pbkdf2 = Pbkdf2(app)
    return pbkdf2


class TestPbkdf2:
    def test_check_password(self, pbkdf2):
        encoded = 'pbkdf2_sha256$1000$tablesalt$8cc051c0f3c5f2e20cdd8fd85d1eb02a911381ff0fa217c0'
        assert pbkdf2.check_password('test', encoded) is True
        with pytest.raises(AssertionError):
            pbkdf2.check_password('test', 'sha1$1000$tablesalt$8cc051c0f3c5f2e20cdd8fd85d1eb02a911381ff0fa217c0')

    def test_make_password(self, pbkdf2):
        encoded = pbkdf2.make_password('test', salt='tablesalt')
        assert encoded == 'pbkdf2_sha256$1000$tablesalt$8cc051c0f3c5f2e20cdd8fd85d1eb02a911381ff0fa217c0'

