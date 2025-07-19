
from .tokenizer import LaTeXTokenizer
from .precedence import PrecedenceManager

class LogicParser:
    """Parser para fórmulas de lógica proposicional"""
    
    def __init__(self, precedence_manager):
        self.precedence_manager = precedence_manager
        self.tokenizer = LaTeXTokenizer()
    
    def parse_to_ast(self, tokens):
        """
        Convierte una lista de tokens a un AST representado como string LaTeX
        
        Args:
            tokens (list): Lista de tokens
            
        Returns:
            str: Expresión LaTeX completamente parentizada
            
        Raises:
            ValueError: Si la expresión está malformada
        """
        if not tokens:
            raise ValueError("No se pueden procesar tokens vacíos")
        
        # Convertir a notación postfija usando algoritmo similar a Shunting Yard
        postfix = self._to_postfix(tokens)
        
        # Construir el AST desde la notación postfija
        result = self._postfix_to_latex(postfix)
        
        return result
    
    def _to_postfix(self, tokens):
        """
        Convierte tokens a notación postfija respetando precedencia
        
        Args:
            tokens (list): Lista de tokens en notación infija
            
        Returns:
            list: Lista de tokens en notación postfija
        """
        output = []
        operator_stack = []
        
        for token in tokens:
            if self.tokenizer.is_operand(token):
                output.append(token)
            elif self.tokenizer.is_operator(token):
                # Sacar operadores con mayor o igual precedencia
                while (operator_stack and 
                       self.tokenizer.is_operator(operator_stack[-1]) and
                       self.precedence_manager.has_greater_or_equal_precedence(
                           operator_stack[-1], token)):
                    output.append(operator_stack.pop())
                
                operator_stack.append(token)
        
        # Vaciar la pila de operadores
        while operator_stack:
            output.append(operator_stack.pop())
        
        return output
    
    def _postfix_to_latex(self, postfix_tokens):
        """
        Convierte notación postfija a LaTeX completamente parentizado
        
        Args:
            postfix_tokens (list): Tokens en notación postfija
            
        Returns:
            str: Expresión LaTeX parentizada
            
        Raises:
            ValueError: Si la expresión está malformada
        """
        stack = []
        
        for token in postfix_tokens:
            if self.tokenizer.is_operand(token):
                stack.append(token)
            elif self.tokenizer.is_unary_operator(token):
                if len(stack) < 1:
                    raise ValueError(f"Operador unario '{token}' requiere un operando")
                
                operand = stack.pop()
                if token == 'neg':
                    stack.append(f"\\neg {operand}")
            elif self.tokenizer.is_binary_operator(token):
                if len(stack) < 2:
                    raise ValueError(f"Operador binario '{token}' requiere dos operandos")
                
                right = stack.pop()
                left = stack.pop()
                
                # Generar la expresión LaTeX apropiada
                latex_expression = self._format_binary_operation(token, left, right)
                stack.append(latex_expression)
        
        if len(stack) != 1:
            raise ValueError("Expresión malformada: la pila final no contiene exactamente un elemento")
        
        return stack[0]
    
    def _format_binary_operation(self, operator, left, right):
        """
        Formatea una operación binaria en LaTeX
        
        Args:
            operator (str): Operador binario
            left (str): Operando izquierdo
            right (str): Operando derecho
            
        Returns:
            str: Expresión LaTeX formateada
        """
        operator_map = {
            'vee': '\\vee',
            'wedge': '\\wedge',
            'rightarrow': '\\rightarrow',
            'leftrightarrow': '\\leftrightarrow'
        }
        
        latex_op = operator_map.get(operator, operator)
        return f"({left} {latex_op} {right})"
