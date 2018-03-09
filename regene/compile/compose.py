from typing import Iterator

from regene.compile.braces import Braces, Brackets, CurlyBraces
from regene.compile.quantifier_factory import QuantifierFactory
from regene.compile.regular_expression import RegularExpression
from regene.expression import Expression
from regene.expression.group import Group
from regene.expression.quantified import Quantified
from regene.expression.string import String


class Composer:
    def __init__(self, expression: RegularExpression):
        self.expression = expression

    def build(self, expression: RegularExpression) -> Iterator[Expression]:
        peeled_list = list(Peeler(expression))
        index = 0

        while index < len(peeled_list):

            if (index + 1 < len(peeled_list) and
                    self.is_quantifier(peeled_list[index + 1])):
                yield self.quantify(index, peeled_list)
                index += 2
                continue

            elif self.is_character_set(peeled_list[index]):
                pass

            elif self.is_group(peeled_list[index]):
                yield self.groupify(index, peeled_list)
                index += 1
                continue

            else:
                yield String(str(peeled_list[index]))
                index += 1
                continue

    def quantify(self, index, peeled_list) -> Expression:
        quantifier = QuantifierFactory.get(peeled_list[index + 1])
        compiled_content = list(self.build(peeled_list[index]))
        # If we need to quantify a String, we quantify the last character
        if type(compiled_content[-1]) is String:
            return Group([
                Group(compiled_content[:-1] + [compiled_content[-1][:-1]]),
                Quantified(compiled_content[-1][-1], quantifier)
            ])

        else:
            quantified = Group(compiled_content)
            return Quantified(quantified, quantifier)

    def groupify(self, index, peeled_list) -> Group:
        groupped_expression = peeled_list[index]
        within_expression = Braces(groupped_expression).within()
        compiled_content = list(self.build(within_expression))
        return Group(compiled_content)

    def enter(self) -> Group:
        """Entry point to the recursive method build()."""
        return Group(list(self.build(self.expression)))

    def is_quantifier(self, expression: RegularExpression) -> bool:
        return any([expression in ("+", "?", "*"),
                    str(expression).startswith("{")])

    def is_character_set(self, expression: RegularExpression) -> bool:
        return str(expression).startswith("[")

    def is_group(self, expression: RegularExpression) -> bool:
        return str(expression).startswith("(")


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
