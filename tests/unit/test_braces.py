from unittest import TestCase

from regene.compile.braces import Braces, CurlyBraces, Brackets


class BracesTest(TestCase):
    def test_simple(self):
        assert Braces("()").indices() == (0, 1)

    def test_nested(self):
        assert Braces("(())").indices() == (0, 3)

    def test_parenthesis_starts_after_0(self):
        assert Braces("f(())").indices() == (1, 4)

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

    def test_after(self):
        assert Braces("A(Hello)B").after() == "B"
        assert Braces("A(Hello)").after() == ""
        assert Braces("(Hello)B").after() == "B"
        assert Braces("AB").after() == "AB"

    def test_before(self):
        assert Braces("A(Hello)B").before() == "A"
        assert Braces("A(Hello)").before() == "A"
        assert Braces("(Hello)B").before() == ""
        assert Braces("AB").before() == ""


class CurlyBracesTest(TestCase):
    def test_simple(self):
        assert CurlyBraces("{}").indices() == (0, 1)

    def test_nested(self):
        assert CurlyBraces("{{}}").indices() == (0, 3)

    def test_parenthesis_starts_after_0(self):
        assert CurlyBraces("f{{}}").indices() == (1, 4)

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

    def test_after(self):
        assert CurlyBraces("A{Hello}B").after() == "B"
        assert CurlyBraces("A{Hello}").after() == ""
        assert CurlyBraces("{Hello}B").after() == "B"
        assert CurlyBraces("AB").after() == "AB"

    def test_before(self):
        assert CurlyBraces("A{Hello}B").before() == "A"
        assert CurlyBraces("A{Hello}").before() == "A"
        assert CurlyBraces("{Hello}B").before() == ""
        assert CurlyBraces("AB").before() == ""


class BracketsTest(TestCase):
    def test_simple(self):
        assert Brackets("[]").indices() == (0, 1)

    def test_nested(self):
        assert Brackets("[[]]").indices() == (0, 3)

    def test_parenthesis_starts_after_0(self):
        assert Brackets("f[[]]").indices() == (1, 4)

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

    def test_after(self):
        assert Brackets("A[Hello]B").after() == "B"
        assert Brackets("A[Hello]").after() == ""
        assert Brackets("[Hello]B").after() == "B"
        assert Brackets("AB").after() == "AB"

    def test_before(self):
        assert Brackets("A[Hello]B").before() == "A"
        assert Brackets("A[Hello]").before() == "A"
        assert Brackets("[Hello]B").before() == ""
        assert Brackets("AB").before() == ""
