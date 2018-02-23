class Expression:
    def __mul__(self, other: int) -> "Expression":
        pass

    def __eq__(self, other):
        return str(self) == str(other)
