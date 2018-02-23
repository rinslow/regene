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

    def __int__(self):
        return self.start

class Exactly(Quantifier):
    def __init__(self, value: int):
        self.value = value

    def quantify(self, expression: Expression) -> Expression:
        return expression * self.value

    def __int__(self):
        return self.value

class OneOrMore(Quantifier):
    def quantify(self, expression: Expression) -> Expression:
        return expression

    def __int__(self):
        return 1


class ZeroOrMore(Quantifier):
    def quantify(self, expression: Expression) -> Expression:
        return EmptyExpression()

    def __int__(self):
        return 0

class ZeroOrOne(Quantifier):
    def quantify(self, expression: Expression) -> Expression:
        return EmptyExpression()

    def __int__(self):
        return 0