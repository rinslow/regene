from regene.compile.compose import Composer
from regene.compile.regular_expression import RegularExpression


class Regene(object):
    def __init__(self, expression: str):
        self.expression = expression

    def random(self) -> str:
        """A random string that would match given expression."""
        raise NotImplementedError("No support for randoms yet.")

    def minimal(self) -> str:
        raise NotImplementedError("No support for minimals yet.")

    def _precompiled_experssion(self):
        # TODO: Remove spaces from quantifiers
        return (self.expression.replace(r"\d", r"[0-9]")
                               .replace(r"\D", r"[^0-9]")
                               .replace(r"\s", r"[ \t\n\f\r]")
                               .replace(r"\S", r"[^ \t\n\f\r]")
                               .replace(r"\w", r"[a-zA-Z_0-9]")
                               .replace(r"\W", r"[^a-zA-Z_0-9]"))

    def simple(self) -> str:
        """Minimal string that would match a given expression."""
        return str(Composer(RegularExpression(self.expression)).enter())
