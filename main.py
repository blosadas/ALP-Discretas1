"""
Analizador de Lógica Proposicional - Punto de entrada principal
Autor: Brandon Losada
"""

from logic.parser import LogicParser
from logic.precedence import PrecedenceManager
from logic.tokenizer import LaTeXTokenizer
from utils.latex_io import LaTeXFormatter

def main():
    """Función principal del programa"""
    try:
        # Inicializar componentes
        precedence_manager = PrecedenceManager("data/tabla.csv")
        tokenizer = LaTeXTokenizer()
        parser = LogicParser(precedence_manager)
        formatter = LaTeXFormatter()
        
        # Obtener entrada del usuario
        print("=== Analizador de Lógica Proposicional ===")
        formula = input("Ingrese la fórmula en LaTeX sin paréntesis: ")
        
        # Procesar la fórmula
        tokens = tokenizer.tokenize(formula)
        result = parser.parse_to_ast(tokens)
        formatted_result = formatter.format_output(result)
        
        # Mostrar resultado
        print("\nFórmula bien formada en LaTeX con paréntesis:")
        print(formatted_result)
        
    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo de tabla de precedencia.")
    except ValueError as e:
        print(f"Error en la fórmula ingresada: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
