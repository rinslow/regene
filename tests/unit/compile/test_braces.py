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
        assert not Braces.exists(RegularExpression("ab"))
        assert Braces.exists(RegularExpression("ab()"))

    def test_all(self):
        assert Braces("A(Hello)B").all() == "(Hello)"
        assert Braces("A((Hello))").all() == "((Hello))"
        assert Braces("((Hello)))B").all() == "((Hello))"

    def test_latest(self):
        assert Braces("(abc)f(def)", latest=0).all() == "(abc)"
        assert Braces("(abc)f(def)", latest=4).all() == "(def)"

    def test_indices(self):
        # assert Braces("(abc)f(def)").indices() == (0, 3)
        assert Braces("(abc)").indices() == (0, 2)
