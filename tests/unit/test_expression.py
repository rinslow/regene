from unittest import TestCase

from regene.expression import Exactly
from regene.expression.character_class import CharacterClassFactory
from regene.expression.quantified import Quantified
from regene.expression.string import String


class MultiplicationTest(TestCase):
    def test_string_multiplication(self):
        assert String("F") * 4 == "FFFF"

    def test_quantified_multiplication(self):
        assert Quantified(String("F"), Exactly(2)) * 2 == "FFFF"

    def test_character_set_multiplication(self):
        assert CharacterClassFactory.get("[abc]") * 4 == "aaaa"

    def test_ranged_character_set_multiplication(self):
        assert CharacterClassFactory.get("[b-z]") * 4 == "bbbb"
