"""
Tests básicos para el analizador de lógica proposicional
"""

import unittest
import sys
import os

# Agregar el directorio padre al path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic.parser import LogicParser
from logic.precedence import PrecedenceManager
from logic.tokenizer import LaTeXTokenizer

class TestLogicParser(unittest.TestCase):
    """Tests para el parser de lógica"""
    
    def setUp(self):
        """Configuración inicial para los tests"""
        self.precedence_manager = PrecedenceManager("data/tabla.csv")
        self.parser = LogicParser(self.precedence_manager)
        self.tokenizer = LaTeXTokenizer()
    
    def test_simple_negation(self):
        """Test para negación simple"""
        tokens = self.tokenizer.tokenize("\\neg p")
        result = self.parser.parse_to_ast(tokens)
        self.assertEqual(result, "\\neg p")
    
    def test_binary_operation(self):
        """Test para operaciones binarias"""
        tokens = self.tokenizer.tokenize("p \\vee q")
        result = self.parser.parse_to_ast(tokens)
        self.assertEqual(result, "(p \\vee q)")
    
    def test_precedence(self):
        """Test para precedencia de operadores"""
        tokens = self.tokenizer.tokenize("p \\vee q \\wedge r")
        result = self.parser.parse_to_ast(tokens)
        self.assertEqual(result, "(p \\vee (q \\wedge r))")

if __name__ == '__main__':
    unittest.main()
