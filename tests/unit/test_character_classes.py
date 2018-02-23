from unittest import TestCase
from regene.expression.character_class import CharacterClassFactory


class TestCharacterSet(TestCase):
    def test_only_characters(self):
        assert str(CharacterClassFactory.get("[abcde]")) == "a"

    def test_a_single_range(self):
        assert str(CharacterClassFactory.get("[0-6]")) == "0"

    def test_multiple_ranges(self):
        assert str(CharacterClassFactory.get("[0-6A-Z]")) == "0"

    def test_mixed_ranges_and_characters(self):
        assert str(CharacterClassFactory.get("[B0-6A-Z]")) == "B"

    def test_mixed_characters_and_ranges(self):
        assert str(CharacterClassFactory.get("[A-ZB0-6]")) == "B"

    def test_dash(self):
        assert str(CharacterClassFactory.get("[\-]")) == "-"