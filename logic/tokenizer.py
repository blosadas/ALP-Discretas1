"""
Módulo para tokenizar fórmulas de lógica proposicional en LaTeX
"""

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
        self.operands = {'p', 'q', 'r'}
        self.all_operators = self.binary_operators.union(self.unary_operators)
    
    def tokenize(self, formula):
        """
        Tokeniza una fórmula LaTeX convirtiéndola en tokens internos
        
        Args:
            formula (str): Fórmula en LaTeX
            
        Returns:
            list: Lista de tokens
            
        Raises:
            ValueError: Si la fórmula contiene tokens inválidos
        """
        if not formula or not formula.strip():
            raise ValueError("La fórmula no puede estar vacía")
        
        # Aplicar reemplazos LaTeX
        processed_formula = formula
        for latex_op, internal_op in self.latex_replacements.items():
            processed_formula = processed_formula.replace(latex_op, internal_op)
        
        # Dividir en tokens
        tokens = processed_formula.split()
        
        # Validar tokens
        self._validate_tokens(tokens)
        
        return tokens
    
    def _validate_tokens(self, tokens):
        """
        Valida que todos los tokens sean reconocidos
        
        Args:
            tokens (list): Lista de tokens a validar
            
        Raises:
            ValueError: Si hay tokens inválidos
        """
        valid_tokens = self.all_operators.union(self.operands)
        
        for token in tokens:
            if token not in valid_tokens:
                raise ValueError(f"Token inválido: '{token}'. "
                               f"Tokens válidos: {sorted(valid_tokens)}")
    
    def is_operand(self, token):
        """Verifica si un token es un operando"""
        return token in self.operands
    
    def is_operator(self, token):
        """Verifica si un token es un operador"""
        return token in self.all_operators
    
    def is_binary_operator(self, token):
        """Verifica si un token es un operador binario"""
        return token in self.binary_operators
    
    def is_unary_operator(self, token):
        """Verifica si un token es un operador unario"""
        return token in self.unary_operators
