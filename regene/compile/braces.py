from typing import Tuple


class Braces:
    OPEN = "("
    CLOSE = ")"

    def __init__(self, string: str):
        self.string = string

    def indices(self) -> Tuple[int, int]:
        try:
            start = self.string.index(self.OPEN)

        except ValueError:
            raise IndexError("No opening %r found" % self.__class__.__name__)

        return (start, self._find_end_by_start_index(start))

    def _find_end_by_start_index(self, index) -> int:
        stack = []
        for index, char in enumerate(self.string[index:]):
            if char == self.OPEN:
                stack.append(char)

            if char == self.CLOSE:
                stack.pop()
                if len(stack) == 0:
                    return index

        raise IndexError("No closing %r found" % self.__class__.__name__)

    def within(self) -> str:
        start, end = self.indices()
        return self.string[start + 1: end]


class Brackets(Braces):
    OPEN = "["
    CLOSE = "]"


class CurlyBraces(Braces):
    OPEN = "{"
    CLOSE = "}"
