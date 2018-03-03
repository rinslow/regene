from unittest import TestCase

from regene.compile.quantifier_factory import QuantifierFactory
from regene.compile.regular_expression import RegularExpression
from regene.expression.string import String


class QuantifierFactoryTest(TestCase):
    def test_plus(self):
        quantifier = QuantifierFactory.get(RegularExpression("+"))
        assert quantifier.quantify(String("4")) == "4"

    def test_question_mark(self):
        quantifier = QuantifierFactory.get(RegularExpression("?"))
        assert quantifier.quantify(String("4")) == ""


    def test_star(self):
        quantifier = QuantifierFactory.get(RegularExpression("*"))
        assert quantifier.quantify(String("4")) == ""


    def test_exactly(self):
        quantifier = QuantifierFactory.get(RegularExpression("{3}"))
        assert quantifier.quantify(String("4")) == "444"


    def test_between(self):
        quantifier = QuantifierFactory.get(RegularExpression("{5, 6}"))
        assert quantifier.quantify(String("4")) == "44444"


    def test_value_or_more(self):
        quantifier = QuantifierFactory.get(RegularExpression("{4,}"))
        assert quantifier.quantify(String("4")) == "4444"


    def test_value_or_less(self):
        quantifier = QuantifierFactory.get(RegularExpression("{, 4}"))
        assert quantifier.quantify(String("4")) == ""

