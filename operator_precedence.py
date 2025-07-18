import csv
from inspect import stack

# Carga la tabla de precedencia desde CSV
def load_precedence_table(filename):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        headers = [h.strip() for h in next(reader)[1:]]
        table = {}
        for row in reader:
            key = row[0].strip()
            values = [cell.strip() for cell in row[1:]]
            table[key] = dict(zip(headers, values))
    return table

# Operadores válidos
BINARY_OPERATORS = {'vee', 'wedge', 'rightarrow', 'leftrightarrow'}
UNARY_OPERATORS = {'neg'}
OPERANDS = {'p', 'q', 'r'}
ALL_OPERATORS = BINARY_OPERATORS.union(UNARY_OPERATORS)

# Construye el AST desde la fórmula y la tabla
def to_ast(tokens, precedence):
    def has_greater_or_equal_prec(op1, op2):
        # op1 es el operador en la pila, op2 es el nuevo operador
        return precedence.get(op1, {}).get(op2, '') in {'>', '='}

    output = []
    ops = []

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in OPERANDS:
            output.append(token)
        elif token in ALL_OPERATORS:
            while ops and ops[-1] in ALL_OPERATORS and has_greater_or_equal_prec(ops[-1], token):
                output.append(ops.pop())
            ops.append(token)
        i += 1

    while ops:
        output.append(ops.pop())

    # Reconstruir el árbol desde la notación postfija
    stack = []
    for token in output:
        if token in OPERANDS:
            stack.append(token)
        elif token in UNARY_OPERATORS:
            operand = stack.pop()
            stack.append(f"\\neg ({operand})")
        elif token in BINARY_OPERATORS:
            right = stack.pop()
            left = stack.pop()
            if token == 'vee':
                stack.append(f"({left} \\vee {right})")
            elif token == 'wedge':
                stack.append(f"({left} \\wedge {right})")
            elif token == 'rightarrow':
                stack.append(f"({left} \\rightarrow {right})")
            elif token == 'leftrightarrow':
                stack.append(f"({left} \\leftrightarrow {right})")
    return stack[0]

# Limpia y tokeniza la entrada
def tokenize_latex(formula):
    replacements = {
        '\\neg': 'neg',
        '\\vee': 'vee',
        '\\wedge': 'wedge',
        '\\rightarrow': 'rightarrow',
        '\\leftrightarrow': 'leftrightarrow',
    }
    for k, v in replacements.items():
        formula = formula.replace(k, v)
    return formula.split()

# Main
if __name__ == "__main__":
    table = load_precedence_table("tabla.csv")
    formula = input("Ingrese la fórmula en LaTeX sin paréntesis: ")
    tokens = tokenize_latex(formula)
    try:
        result = to_ast(tokens, table)
        print("Fórmula bien formada en LaTeX con paréntesis:")
        print(result)
    except Exception as e:
        print("Error:", e)
