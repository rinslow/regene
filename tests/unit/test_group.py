from unittest import TestCase

from regene.expression import Exactly
from regene.expression.group import Group
from regene.expression.string import String


class GroupTest(TestCase):
    def test_str(self):
        assert Group(String("1"), Exactly(1)) == "1"

    def test_quantifiers(self):
        assert Group(String("A"), Exactly(2)) == "AA"

    def test_group_within_a_group(self):
        assert Group(
            Group(String("A"), Exactly(1)),
            Exactly(1)) == "A"

    def test_multiplication(self):
        assert (Group(String("1"), Exactly(1)) * 2) * 2 == "1111"
