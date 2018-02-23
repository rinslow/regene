from unittest import TestCase

from regene.expression import Between, Exactly, ZeroOrOne, ZeroOrMore, OneOrMore
from regene.expression.string import String


class TestQuantifiers(TestCase):
    def test_between(self):
        assert Between(1, 4).quantify(String("f")) == "f"
        assert Between(0, 4).quantify(String("f")) == ""
        assert Between(2, 4).quantify(String("f")) == "ff"

    def test_exactly(self):
        assert Exactly(1).quantify(String("1")) == "1"
        assert Exactly(0).quantify(String("1")) == ""
        assert Exactly(2).quantify(String("1")) == "11"

    def test_one_or_more(self):
        assert OneOrMore().quantify(String("111")) == "111"

    def test_zero_or_more(self):
        assert ZeroOrMore().quantify(String("1")) == ""

    def test_zero_or_one(self):
        assert ZeroOrOne().quantify(String("1")) == ""

