import csv


class PrecedenceManager:
    """Maneja la tabla de precedencia entre operadores."""

    def __init__(self, csv_file):
        """Carga la tabla desde un archivo CSV."""
        self.precedence_table = self._load_precedence_table(csv_file)

    def _load_precedence_table(self, filename):
        """Lee y convierte el CSV en un diccionario anidado."""
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
        """True si op1 ≥ op2 en prioridad."""
        return self.precedence_table.get(op1, {}).get(op2, '') in {'>', '='}

    def get_precedence_relation(self, op1, op2):
        """Devuelve la relación entre op1 y op2: '>', '<' o '='."""
        return self.precedence_table.get(op1, {}).get(op2, '')
