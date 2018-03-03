from unittest import TestCase

from regene import Regene


class StringTest(TestCase):
    def test_single_character(self):
        assert Regene("a").simple() == "a"

    def test_multiple_characters(self):
        assert Regene("abc").simple() == "abc"

    def test_empty_string(self):
        assert Regene("").simple() == ""
