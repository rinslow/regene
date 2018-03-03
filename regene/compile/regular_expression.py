import re
from typing import List, Union, Iterator

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

    def __iter__(self) -> Iterator[str]:
        return iter(self.parts())

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(self.string)

    def __bool__(self):
        return bool(self.string)

    def __len__(self):
        return len(self.parts())

    def __getitem__(self, item):
        return RegularExpression(self.parts()[item])

    @lru_cache(maxsize=None)
    def parts(self) -> List[str]:
        result = re.findall("[a-zA-Z0-9]-[a-zA-Z0-9]|"  # sets
                            "{\d+}|"
                            "{\d+,}|"
                            "{,\d+}|"
                            "{\d+,\d+}|"
                            "\w+|"  # string
                            "\)|\(|"  # braces
                            "\]|\[|"  # braces
                            "[+?*]|"  # quantifiers
                            "[\^]",
                            self.string)
        return result
