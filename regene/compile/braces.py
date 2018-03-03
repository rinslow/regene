from typing import Tuple, Union

from regene.compile.regular_expression import RegularExpression


class Braces:
    OPEN = "("
    CLOSE = ")"

    def __init__(self, expression: Union[RegularExpression, str],
                 latest: int=0):
        if isinstance(expression, str):
            expression = RegularExpression(expression)

        self.expression = expression
        self.latest = latest

    def indices(self) -> Tuple[int, int]:
        return (self.start_index(), self.end_index())

    def start_index(self) -> int:
        for index, part in enumerate(self.expression[self.latest:]):
            if part == self.OPEN:
                return index + self.latest

        raise IndexError("No opening %r found" % self.__class__.__name__)

    def end_index(self) -> int:
        braces_depth = 0
        start_index = self.start_index()

        for index, char in enumerate(self.expression.parts()[start_index:]):
            if char == self.OPEN:
                braces_depth += 1

            if char == self.CLOSE:
                braces_depth -= 1
                if braces_depth == 0:
                    return index + start_index

        raise IndexError("No closing %r found" % self.__class__.__name__)

    def within(self) -> RegularExpression:
        try:
            start, end = self.indices()
            parts_within = self.expression.parts()[start + 1: end]
            return RegularExpression(parts_within)

        except IndexError:
            return RegularExpression("")

    def before(self) -> RegularExpression:
        try:
            start = self.start_index()
            parts_before = self.expression.parts()[:start]
            return RegularExpression(parts_before)

        except IndexError:
            return RegularExpression("")

    def after(self) -> RegularExpression:
        try:
            start, end = self.indices()
            parts_after = self.expression.parts()[end + 1:]
            return RegularExpression(parts_after)

        except IndexError:
            return self.expression

    def all(self) -> RegularExpression:
        start, end = self.indices()
        parts = self.expression.parts()[start: end + 1]
        return RegularExpression(parts)

    @classmethod
    def exists(cls, expression: RegularExpression):
        try:
            cls(expression).indices()
            return True

        except IndexError:
            return False


class Brackets(Braces):
    OPEN = "["
    CLOSE = "]"


class CurlyBraces(Braces):
    OPEN = "{"
    CLOSE = "}"
