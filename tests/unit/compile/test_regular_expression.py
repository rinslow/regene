from unittest import TestCase

from regene.compile.regular_expression import RegularExpression


class RegularExpressionsPartsTest(TestCase):
    def test_string(self):
        assert RegularExpression("abc").parts() == ["abc"]
        assert RegularExpression("abc4").parts() == ["abc4"]

    def test_braces(self):
        # Braces
        assert RegularExpression("(").parts() == ["("]
        assert RegularExpression("()").parts() == ["(", ")"]
        assert RegularExpression(")))(").parts() == [")", ")", ")", "("]

        # Brackets
        assert RegularExpression("[").parts() == ["["]
        assert RegularExpression("[]").parts() == ["[", "]"]
        assert RegularExpression("]]][").parts() == ["]", "]", "]", "["]

        # Curly Braces
        assert RegularExpression("{").parts() == ["{"]
        assert RegularExpression("{}").parts() == ["{", "}"]
        assert RegularExpression("}}}{").parts() == ["}", "}", "}", "{"]

    def test_quantifiers(self):
        assert RegularExpression("**??++?+?*").parts() == ["*", "*", "?", "?",
                                                           "+", "+", "?", "+",
                                                           "?", "*", ]

    def test_character_sets(self):
        assert RegularExpression("a-zA-Z").parts() == ["a-z", "A-Z"]

    def test_complex_regular_expressions(self):
        assert RegularExpression("(abc)+").parts() == ["(", "abc", ")", "+"]
        assert RegularExpression("[^A-Zd]+?").parts() == ["[", "^", "A-Z",
                                                          "d", "]", "+", "?"]
