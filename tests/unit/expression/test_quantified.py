from unittest import TestCase

from regene.expression import Exactly
from regene.expression.quantified import Quantified
from regene.expression.string import String


class QuantifiedTest(TestCase):
    def test_str(self):
        assert Quantified(String("1"), Exactly(1)) == "1"

    def test_quantifiers(self):
        assert Quantified(String("A"), Exactly(2)) == "AA"

    def test_group_within_a_group(self):
        assert Quantified(
            Quantified(String("A"), Exactly(1)),
            Exactly(1)) == "A"

    def test_multiplication(self):
        assert (Quantified(String("1"), Exactly(1)) * 2) * 2 == "1111"
