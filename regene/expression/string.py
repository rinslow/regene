from regene.expression import Expression


class EmptyExpression(Expression):
    def __str__(self):
        return str()

    def __mul__(self, other):
        return self


class String(Expression):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __mul__(self, other):
        return String(self.value * other)

    def __getitem__(self, item):
        return self.value[item]
