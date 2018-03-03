import re

from regene.compile.braces import CurlyBraces
from regene.compile.regular_expression import RegularExpression
from regene.expression import (Quantifier, OneOrMore, ZeroOrOne, ZeroOrMore,
                               Exactly, Between, ValueOrLess, ValueOrMore)


class QuantifierFactory:
    @classmethod
    def get(cls, expression: RegularExpression) -> Quantifier:
        if expression == "+":
            return OneOrMore()

        if expression == "?":
            return ZeroOrOne()

        if expression == "*":
            return ZeroOrMore()

        if re.match("\{\d+\}", str(expression)):
            return Exactly(*(map(int, re.findall("\d+", str(expression)))))

        if re.match("\{\d+,\s*\d+\}", str(expression)):
            return Between(*map(int, re.findall("\d+", str(expression))))

        if re.match("\{\d+,\s*\}", str(expression)):
            return ValueOrMore(*map(int, re.findall("\d+", str(expression))))

        if re.match("\{\s*,\s*\d+\}", str(expression)):
            return ValueOrLess(*map(int, re.findall("\d+", str(expression))))

        raise ValueError("Unknown quantifier: {expression}"
                         .format(expression=expression))
