from regene.expression import Expression


class Regene(object):
    def __init__(self, expression: str):
        self.expression = expression

    def random(self) -> str:
        """A random string that would match given expression."""
        raise NotImplementedError("No support for randoms yet.")

    def _precompiled_experssion(self):
        return (self.expression.replace(r"\d", r"[0-9]")
                               .replace(r"\D", r"[^0-9]")
                               .replace(r"\s", r"[ \t\n\f\r]")
                               .replace(r"\S", r"[^ \t\n\f\r]")
                               .replace(r"\w", r"[a-zA-Z_0-9]")
                               .replace(r"\W", r"[^a-zA-Z_0-9]"))

    def minimal(self) -> str:
        """Minimal string that would match a given expression."""
        return Expression(self._precompiled_experssion()).suggest()
