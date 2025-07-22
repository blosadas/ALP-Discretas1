"""
Módulo para tokenizar fórmulas de lógica proposicional en LaTeX
"""
import string
class LaTeXTokenizer:
    """Tokenizador para fórmulas LaTeX de lógica proposicional"""
    
    def __init__(self):
        """Inicializa el tokenizador con las reglas de reemplazo"""
        self.latex_replacements = {
            '\\neg': 'neg',
            '\\vee': 'vee',
            '\\wedge': 'wedge',
            '\\rightarrow': 'rightarrow',
            '\\leftrightarrow': 'leftrightarrow',
        }
        
        # Operadores y operandos válidos
        self.binary_operators = {'vee', 'wedge', 'rightarrow', 'leftrightarrow'}
        self.unary_operators = {'neg'}
        self.operands = set(string.ascii_lowercase)
        self.all_operators = self.binary_operators.union(self.unary_operators)
    
    def tokenize(self, formula):
        """Convierte una fórmula LaTeX en una lista de tokens internos."""
        if not formula or not formula.strip():
            raise ValueError("La fórmula no puede estar vacía")

        processed = formula
        for latex_op, internal_op in self.latex_replacements.items():
            processed = processed.replace(latex_op, internal_op)

        tokens = processed.split()
        self._validate_tokens(tokens)
        return tokens

    def _validate_tokens(self, tokens):
        """Lanza error si algún token no es válido."""
        valid = self.all_operators.union(self.operands)
        for token in tokens:
            if token not in valid:
                raise ValueError(f"Token inválido: '{token}'. Válidos: {sorted(valid)}")

    def is_operand(self, token):
        return token in self.operands

    def is_operator(self, token):
        return token in self.all_operators

    def is_binary_operator(self, token):
        return token in self.binary_operators

    def is_unary_operator(self, token):
        return token in self.unary_operators