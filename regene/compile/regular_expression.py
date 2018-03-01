import re
from typing import List

from regene.compile.braces import Braces, Brackets, CurlyBraces
from regene.expression import Expression
from regene.expression.group import Group


class RegularExpression:
    def __init__(self, string: str):
        self.string = string

    def parts(self) -> List[str]:
        result = re.findall("[a-zA-Z0-9]\-[a-zA-Z0-9]|"  # sets
                            "\w+|"  # string
                            "\)|\(|"  # braces
                            "\]|\[|"  # braces
                            "\}|\{|"  # braces
                            "[\+\?\*]",  # quantifiers
                            self.string)
        return result
