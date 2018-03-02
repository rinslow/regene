from typing import Tuple, Union

from regene.compile.regular_expression import RegularExpression


class Braces:
    OPEN = "("
    CLOSE = ")"

    def __init__(self, expression: Union[RegularExpression, str]):
        if isinstance(expression, str):
            expression = RegularExpression(expression)

        self.expression = expression

    def _indices(self) -> Tuple[int, int]:
        try:
            start = self.expression.parts().index(self.OPEN)

        except ValueError:
            raise IndexError("No opening %r found" % self.__class__.__name__)

        return (start, self._find_end_by_start_index(start))

    def _find_end_by_start_index(self, start_index) -> int:
        stack = []
        for index, char in enumerate(self.expression.parts()[start_index:]):
            if char == self.OPEN:
                stack.append(char)

            if char == self.CLOSE:
                stack.pop()
                if len(stack) == 0:
                    return index + start_index

        raise IndexError("No closing %r found" % self.__class__.__name__)

    def within(self) -> RegularExpression:
        try:
            start, end = self._indices()
            parts_within = self.expression.parts()[start + 1: end]
            return RegularExpression(parts_within)

        except IndexError:
            return RegularExpression("")

    def before(self) -> RegularExpression:
        try:
            start, _ = self._indices()
            parts_before = self.expression.parts()[:start]
            return RegularExpression(parts_before)

        except IndexError:
            return RegularExpression("")

    def after(self) -> RegularExpression:
        try:
            start, end = self._indices()
            parts_after = self.expression.parts()[end + 1:]
            return RegularExpression(parts_after)

        except IndexError:
            return self.expression

    @classmethod
    def exists(cls, string: str):
        try:
            cls(string)._indices()
            return True

        except IndexError:
            return False


class Brackets(Braces):
    OPEN = "["
    CLOSE = "]"


class CurlyBraces(Braces):
    OPEN = "{"
    CLOSE = "}"
