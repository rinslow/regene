from unittest import TestCase

from regene import Regene


class StringTest(TestCase):
    def test_single_character(self):
        assert Regene("a").simple() == "a"

    def test_multiple_characters(self):
        assert Regene("abc").simple() == "abc"

    def test_empty_string(self):
        assert Regene("").simple() == ""


class QuantifierTest(TestCase):
    def test_plus(self):
        assert Regene("ab+").simple() == "ab"

    def test_question_mark(self):
        assert Regene("ab?").simple() == "a"

    def test_star(self):
        assert Regene("ab*c").simple() == "ac"

    def test_between(self):
        assert Regene("a{4,5}b").simple() == "aaaab"

    def test_exactly(self):
        assert Regene("abc{2}").simple() == "abcc"

    def test_value_or_more(self):
        assert Regene("ab{1,}").simple() == "ab"

    def test_value_or_less(self):
        assert Regene("ab{,6}").simple() == "a"


class GroupTest(TestCase):
    def test_group_plus(self):
        assert Regene("(ab)+").simple() == "ab"

    def test_group_question_mark(self):
        assert Regene("(ab)?").simple() == ""

    def test_group_star(self):
        assert Regene("(ab)*c").simple() == "c"

    def test_group_between(self):
        assert Regene("(ab){4,5}").simple() == "abababab"

    def test_group_exactly(self):
        assert Regene("a(bc){2}").simple() == "abcbc"

    def test_group_value_or_more(self):
        assert Regene("(abc){3,}").simple() == "abcabcabc"

    def test_group_value_or_less(self):
        assert Regene("a(b){,6}").simple() == "a"
