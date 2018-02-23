from regene.expression import Expression, Quantifier, Exactly


class Group(Expression):
    def __init__(self, expression: Expression, quantifier: Quantifier):
        self.value = quantifier.quantify(expression)

    def __mul__(self, other):
        return self.value * other

    def __str__(self):
        return str(self.value)
