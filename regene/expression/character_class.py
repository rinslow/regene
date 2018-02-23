from typing import List, Tuple

from regene.expression import Expression
from regene.expression.string import String


class CharacterClass(Expression):
    def __init__(self, characters: List[str]):
        self.characters = characters

    def __str__(self):
        return self.characters[0]

    def __mul__(self, other):
        return String(str(self)) * other

class RangedCharacterClass(Expression):
    def __init__(self, ranges: List[Tuple[str, str]], characters: List[str]):
        self.ranges = ranges
        self.characters = characters

    def __mul__(self, other):
        return String(str(self)) * other

    def __str__(self):
        if self.characters:
            return self.characters[0]

        return self.ranges[0][0]


class CharacterClassFactory:
    @classmethod
    def get(cls, string: str) -> Expression:
        if not string.startswith("[") or not string.endswith("]"):
            raise TypeError("Cannot parse a character class that does not "
                            "start and end with square brackets")

        characters, ranges = cls.parse_string(string[1:-1])

        if not ranges:
            return CharacterClass(characters)

        return RangedCharacterClass(ranges, characters)

    @classmethod
    def parse_string(cls, string: str) -> Tuple[List[str],
                                                List[Tuple[str, str]]]:
        ranges = []
        characters = []
        index = -1
        while index < len(string) - 1:
            index += 1

            # We're parsing a range
            if (index < len(string) - 1 and
                string[index + 1] == "-" and
                string[index] != "\\"):

                ranges += (string[index], string[index + 2])
                index += 2
                continue

            # We're parsing an escaped character
            if string[index] == "\\":
                characters.append(string[index + 1])
                index += 1
                continue

            # We're parsing a regular character
            characters.append(string[index])
            continue

        return characters, ranges
