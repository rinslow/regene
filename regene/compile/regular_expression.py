import re
from typing import List, Union

from functools import lru_cache


class RegularExpression:
    def __init__(self, regex: Union[str, List[str]]):
        if type(regex) is list:
            regex = "".join(regex)

        self.string = regex

    def __str__(self):
        return self.string

    def __repr__(self):
        return repr(self.string)

    def __iter__(self):
        return iter(self.string)

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(self.string)

    @lru_cache(maxsize=None)
    def parts(self) -> List[str]:
        result = re.findall("[a-zA-Z0-9]-[a-zA-Z0-9]|"  # sets
                            "\w+|"  # string
                            "\)|\(|"  # braces
                            "\]|\[|"  # braces
                            "}|{|"  # braces
                            "[+?*]|"  # quantifiers
                            "[\^]",
                            self.string)
        return result
