from regene.expression import Expression
from typing import List

from regene.expression.string import String


class Group(Expression):
    def __init__(self, expressions: List[Expression]):
        self.expressions = expressions

    def __mul__(self, other: int):
        return String(str(self)) * other

    def __str__(self):
        return "".join(str(expression) for expression in self.expressions)
