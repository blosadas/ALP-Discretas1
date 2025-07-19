"""
Módulo para manejar la tabla de precedencia de operadores lógicos
"""

import csv

class PrecedenceManager:
    """Maneja la tabla de precedencia de operadores lógicos"""
    
    def __init__(self, csv_file):
        """
        Inicializa el manager con una tabla de precedencia desde CSV
        
        Args:
            csv_file (str): Ruta al archivo CSV con la tabla de precedencia
        """
        self.precedence_table = self._load_precedence_table(csv_file)
    
    def _load_precedence_table(self, filename):
        """
        Carga la tabla de precedencia desde un archivo CSV
        
        Args:
            filename (str): Nombre del archivo CSV
            
        Returns:
            dict: Tabla de precedencia como diccionario anidado
            
        Raises:
            FileNotFoundError: Si el archivo no existe
        """
        try:
            with open(filename, newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                headers = [h.strip() for h in next(reader)[1:]]
                table = {}
                
                for row in reader:
                    key = row[0].strip()
                    values = [cell.strip() for cell in row[1:]]
                    table[key] = dict(zip(headers, values))
                
                return table
        except FileNotFoundError:
            raise FileNotFoundError(f"No se pudo encontrar el archivo {filename}")
    
    def has_greater_or_equal_precedence(self, op1, op2):
        """
        Verifica si op1 tiene mayor o igual precedencia que op2
        
        Args:
            op1 (str): Primer operador
            op2 (str): Segundo operador
            
        Returns:
            bool: True si op1 tiene mayor o igual precedencia que op2
        """
        return self.precedence_table.get(op1, {}).get(op2, '') in {'>', '='}
    
    def get_precedence_relation(self, op1, op2):
        """
        Obtiene la relación de precedencia entre dos operadores
        
        Args:
            op1 (str): Primer operador
            op2 (str): Segundo operador
            
        Returns:
            str: Relación de precedencia ('>', '<', '=')
        """
        return self.precedence_table.get(op1, {}).get(op2, '')
