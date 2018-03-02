from unittest import TestCase

from regene.compile.braces import Braces

# No point in testing Brackets and CurlyBraces
from regene.compile.regular_expression import RegularExpression


class BracesTest(TestCase):
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

    def test_exists(self):
        assert not Braces.exists("ab")
        assert Braces.exists("ab()")
