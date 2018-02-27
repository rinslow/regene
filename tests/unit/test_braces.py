from unittest import TestCase

from regene.compile.braces import Braces, CurlyBraces, Brackets


class BracesTest(TestCase):
    def test_simple(self):
        assert Braces("()").indices() == (0, 1)

    def test_nested(self):
        assert Braces("(())").indices() == (0, 3)

    def test_bad_cases(self):
        with self.assertRaises(IndexError):
            Braces("(").indices()

        with self.assertRaises(IndexError):
            Braces(")").indices()

        with self.assertRaises(IndexError):
            Braces("(()").indices()

    def test_within(self):
        assert Braces("(Hello)").within() == "Hello"
        assert Braces("((Hello))()").within() == "(Hello)"


class CurlyBracesTest(TestCase):
    def test_simple(self):
        assert CurlyBraces("{}").indices() == (0, 1)

    def test_nested(self):
        assert CurlyBraces("{{}}").indices() == (0, 3)

    def test_bad_cases(self):
        with self.assertRaises(IndexError):
            CurlyBraces("{").indices()

        with self.assertRaises(IndexError):
            CurlyBraces("}").indices()

        with self.assertRaises(IndexError):
            CurlyBraces("{{}").indices()

    def test_within(self):
        assert CurlyBraces("{Hello}").within() == "Hello"
        assert CurlyBraces("{{Hello}}{}").within() == "{Hello}"


class BracketsTest(TestCase):
    def test_simple(self):
        assert Brackets("[]").indices() == (0, 1)

    def test_nested(self):
        assert Brackets("[[]]").indices() == (0, 3)

    def test_bad_cases(self):
        with self.assertRaises(IndexError):
            Brackets("[").indices()

        with self.assertRaises(IndexError):
            Brackets("]").indices()

        with self.assertRaises(IndexError):
            Brackets("[[]").indices()

    def test_within(self):
        assert Brackets("[Hello]").within() == "Hello"
        assert Brackets("[[Hello]][]").within() == "[Hello]"
