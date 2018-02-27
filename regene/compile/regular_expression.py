from regene.compile.braces import Braces, Brackets, CurlyBraces
from regene.expression import Expression
from regene.expression.group import Group
from regene.expression.string import String


class RegularExpressionCompiler:
    def __init__(self, string: str):
        self.string = string

    def haystack(self) -> Expression:
        return Group([self.compile(self.string)])

    def compile(self, string) -> Expression:
        pass
