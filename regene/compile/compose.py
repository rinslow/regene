from typing import Iterator

from regene.compile.braces import Braces, Brackets, CurlyBraces
from regene.compile.regular_expression import RegularExpression


class Composer:
    pass


class Peeler:
    def __init__(self, expression: RegularExpression):
        self.expression = expression

    def __iter__(self) -> Iterator[RegularExpression]:
        index = 0
        latest_braces_index = 0
        latest_brackets_index = 0
        latest_curly_braces_index = 0

        while index < len(self.expression):
            next_index = -1  # Turn off jumping

            current_part = self.expression[index]

            if current_part == '(':
                braces = Braces(self.expression, latest_braces_index)
                yield braces.all()
                next_index = braces.end_index()
                latest_braces_index = next_index

            elif current_part == '[':
                brackets = Brackets(self.expression, latest_brackets_index)
                yield brackets.all()
                next_index = brackets.end_index()
                latest_brackets_index = next_index

            elif current_part == '{':
                curly_braces = CurlyBraces(self.expression,
                                           latest_curly_braces_index)
                yield curly_braces.all()
                next_index = curly_braces.end_index()
                latest_curly_braces_index = next_index

            else:
                yield current_part

            # Should we jump?
            if next_index != -1:
                index = next_index + 1

            else:
                index += 1
