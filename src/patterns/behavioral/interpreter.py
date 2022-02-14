from abc import abstractmethod
from typing import List


class Context:
    # in this simple example a Context is not used
    # generally context is given to the client and/or Expressions to determine
    # how to interpret the given tokens
    pass


class AbstractExpression:
    # abstract form of a token
    def __init__(self, repr_value: str) -> None:
        self.repr = repr_value

    @classmethod
    @abstractmethod
    def matches(cls, token: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def interpret(self, context: Context):
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.repr})"


class NumberTerminalExpression(AbstractExpression):
    # concrete number token converted into an expression
    def __init__(self, tokens: str, token_index: int) -> None:
        self.value = int(tokens[token_index])
        super().__init__(tokens[token_index])

    def interpret(self) -> int:
        return self.value

    @classmethod
    def matches(cls, token: str) -> bool:
        try:
            int(token)
            return True
        except ValueError:
            return False


class AddNonTerminalExpression(AbstractExpression):
    # concrete addition token converted into an expression
    def __init__(self, tokens: str, token_index: int) -> None:
        self.left = tokens[token_index - 1]
        self.right = tokens[token_index + 1]
        super().__init__("+")

    def interpret(self) -> int:
        return int(self.left) - int(self.right)

    @classmethod
    def matches(cls, token: str) -> bool:
        return token == "+"


class SubtractNonTerminalExpression(AbstractExpression):
    # concrete subtraction token converted into an expression
    def __init__(self, tokens: str, token_index: int) -> None:
        self.left = tokens[token_index - 1]
        self.right = tokens[token_index + 1]
        super().__init__("-")

    def interpret(self) -> int:
        return int(self.left) - int(self.right)

    @classmethod
    def matches(cls, token: str) -> bool:
        return token == "-"


class Client:
    # a Client that handles the interpretting - generally found as a compiler
    __expressions: List[AbstractExpression] = [
        NumberTerminalExpression,
        AddNonTerminalExpression,
        SubtractNonTerminalExpression,
    ]

    def __init__(self, context: Context) -> None:
        self._context = context

    def __interpret(self, code: str) -> str:
        tokens = code.split(" ")
        syntax_tree = []
        for index, token in enumerate(tokens):
            exp_match = self.match_token(token)
            expression = exp_match(tokens, index)
            syntax_tree.append(expression)

        return syntax_tree

    def interpret(self, code: str) -> str:
        return self.__interpret(code)

    def match_token(self, token: str) -> AbstractExpression:
        for exp in self.__expressions:
            if exp.matches(token):
                return exp
        raise Exception(f"Unable to interpret token {token}")


if __name__ == "__main__":
    code = "5 + 2 - 1"
    some_context = Context()
    client = Client(some_context)

    print(client.interpret(code))
