from regene.expression import Expression
from regene.expression.string import EmptyExpression


class Quantifier:
    def quantify(self, expression: Expression) -> Expression:
        pass


class Between(Quantifier):
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def quantify(self, expression: Expression) -> Expression:
        return expression * self.start


class Exactly(Quantifier):
    def __init__(self, value: int):
        self.value = value

    def quantify(self, expression: Expression) -> Expression:
        return expression * self.value


class OneOrMore(Quantifier):
    def quantify(self, expression: Expression) -> Expression:
        return expression


class ZeroOrMore(Quantifier):
    def quantify(self, expression: Expression) -> Expression:
        return EmptyExpression()


class ZeroOrOne(Quantifier):
    def quantify(self, expression: Expression) -> Expression:
        return EmptyExpression()


class ValueOrMore(Quantifier):
    def __init__(self, value):
        self.value = value

    def quantify(self, expression: Expression):
        return expression * self.value


class ValueOrLess(Quantifier):
    def __init__(self, value):
        self.value = value

    def quantify(self, expression: Expression):
        return EmptyExpression()
