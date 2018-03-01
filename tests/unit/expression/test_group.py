from unittest import TestCase

from regene.expression import Exactly
from regene.expression.group import Group
from regene.expression.quantified import Quantified
from regene.expression.string import String


class GroupTest(TestCase):
    def test_empty_group(self):
        assert Group([]) == ""

    def test_group_with_a_single_item(self):
        assert Group([String("abc")]) == "abc"

    def test_group_with_multiple_items(self):
        assert Group([String("abc"),
                      Quantified(String("def"),
                                 Exactly(2))]) == "abcdefdef"

    def test_group_within_a_group(self):
        assert Group([Group([String("abc")])]) == "abc"


class GroupMultiplicationTest(TestCase):
    def test_empty_group_multiplication(self):
        assert Group([]) * 4 == ""

    def test_group_with_a_single_item_multiplication(self):
        assert Group([String("abc")]) * 2 == "abcabc"

    def test_group_with_multiple_items_multiplication(self):
        assert Group([String("abc"),
                      Quantified(String("def"),
                                 Exactly(2))]) * 2 == "abcdefdefabcdefdef"

    def test_group_within_a_group_multiplication(self):
        assert Group([Group([String("abc")])]) * 2 == "abcabc"
