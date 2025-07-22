from .tokenizer import LaTeXTokenizer
from .precedence import PrecedenceManager


class LogicParser:
    """Parser de fórmulas proposicionales en LaTeX."""

    def __init__(self, precedence_manager):
        self.precedence_manager = precedence_manager
        self.tokenizer = LaTeXTokenizer()

    def parse_to_ast(self, tokens):
        """
        Devuelve una fórmula bien formada (parentizada) en LaTeX.
        """
        if not tokens:
            raise ValueError("No se pueden procesar tokens vacíos")

        postfix = self._to_postfix(tokens)
        return self._postfix_to_latex(postfix)

    def _to_postfix(self, tokens):
        """
        Convierte una expresión en notación infija a postfija.
        """
        output = []
        operator_stack = []

        for token in tokens:
            if self.tokenizer.is_operand(token):
                output.append(token)
            elif self.tokenizer.is_operator(token):
                while (
                    operator_stack
                    and self.tokenizer.is_operator(operator_stack[-1])
                    and self.precedence_manager.has_greater_or_equal_precedence(
                        operator_stack[-1], token
                    )
                ):
                    output.append(operator_stack.pop())

                operator_stack.append(token)

        # Agrega operadores restantes
        output.extend(reversed(operator_stack))
        return output

    def _postfix_to_latex(self, postfix_tokens):
        """
        Convierte una expresión postfija a LaTeX con paréntesis.
        """
        stack = []

        for token in postfix_tokens:
            if self.tokenizer.is_operand(token):
                stack.append(token)

            elif self.tokenizer.is_unary_operator(token):
                if len(stack) < 1:
                    raise ValueError(f"'{token}' requiere un operando")

                operand = stack.pop()
                stack.append(f"\\neg {operand}")

            elif self.tokenizer.is_binary_operator(token):
                if len(stack) < 2:
                    raise ValueError(f"'{token}' requiere dos operandos")

                right = stack.pop()
                left = stack.pop()
                stack.append(self._format_binary_operation(token, left, right))

        if len(stack) != 1:
            raise ValueError("Expresión malformada")

        return stack[0]

    def _format_binary_operation(self, operator, left, right):
        """
        Devuelve la expresión binaria en LaTeX.
        """
        symbol = {
            "vee": "\\vee",
            "wedge": "\\wedge",
            "rightarrow": "\\rightarrow",
            "leftrightarrow": "\\leftrightarrow",
        }.get(operator, operator)

        return f"({left} {symbol} {right})"
