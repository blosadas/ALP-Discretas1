class LaTeXFormatter:
    """Formatea y valida expresiones LaTeX para lógica proposicional."""

    def __init__(self):
        pass

    def format_output(self, latex_expression):
        """Retorna la expresión formateada."""
        return latex_expression

    def clean_latex(self, expression):
        """Elimina espacios extra en la expresión."""
        return ' '.join(expression.split())

    def validate_latex_syntax(self, expression):
        """Verifica que los paréntesis estén balanceados."""
        return expression.count('(') == expression.count(')')
