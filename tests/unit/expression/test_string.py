from unittest import TestCase

from regene.expression.string import String, EmptyExpression


class StringTest(TestCase):
    def test_string_multiplication(self):
        assert String("F") * 4 == "FFFF"


class EmptyTest(TestCase):
    def test_empty_multiplication(self):
        assert EmptyExpression() == ""
