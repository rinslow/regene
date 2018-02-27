from unittest import TestCase

from regene.expression.string import String


class StringTest(TestCase):
    def test_string_multiplication(self):
        assert String("F") * 4 == "FFFF"
