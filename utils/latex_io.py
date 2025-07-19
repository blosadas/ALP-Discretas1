"""
Utilidades para formateo y manipulación de LaTeX
"""

class LaTeXFormatter:
    """Formateador para salidas LaTeX"""
    
    def __init__(self):
        """Inicializa el formateador"""
        pass
    
    def format_output(self, latex_expression):
        """
        Formatea la salida final
        
        Args:
            latex_expression (str): Expresión LaTeX
            
        Returns:
            str: Expresión formateada
        """
        return latex_expression
    
    def clean_latex(self, expression):
        """
        Limpia y normaliza una expresión LaTeX
        
        Args:
            expression (str): Expresión a limpiar
            
        Returns:
            str: Expresión limpia
        """
        # Remover espacios extra
        cleaned = ' '.join(expression.split())
        return cleaned
    
    def validate_latex_syntax(self, expression):
        """
        Valida básicamente la sintaxis LaTeX
        
        Args:
            expression (str): Expresión a validar
            
        Returns:
            bool: True si es válida
        """
        # Verificaciones básicas de sintaxis LaTeX
        open_parens = expression.count('(')
        close_parens = expression.count(')')
        
        return open_parens == close_parens
