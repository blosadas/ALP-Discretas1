# Analizador de Lógica Proposicional en LaTeX

Este proyecto procesa fórmulas de lógica proposicional escritas en LaTeX (sin paréntesis) y devuelve una versión **completamente parentizada**, respetando la jerarquía de operadores lógicos definida en una tabla de configuración (`tabla.csv`). Es una herramienta útil para estudiantes y docentes de lógica matemática o disciplinas relacionadas.

---

## Características principales

- Soporte para operadores lógicos en notación LaTeX:
  - Negación: `\neg`
  - Conjunción: `\wedge`
  - Disyunción: `\vee`
  - Implicación: `\rightarrow`
  - Bicondicional: `\leftrightarrow`
- Construcción automática de expresiones bien formadas
- Aplicación de precedencia según archivo `tabla.csv`
- Modularidad para facilitar extensión y mantenimiento
- Posibilidad de modificar tanto los operadores válidos como sus jerarquías

---

## Estructura del proyecto
```
analizador_logico/
├── data/
│   └── tabla.csv
├── docs/
│   └── Manual_de_uso.pdf
├── logic/
│   ├── __init__.py
│   ├── parser.py
│   ├── precedence.py
│   └── tokenizer.py
├── utils/
│   ├── __init__.py
│   └── latex_io.py
├── tests/
│   └── test_parser.py
├── main.py
├── README.md
└── .gitignore
```
---

## Uso rápido

1. **Clonar el repositorio**
```
  git clone https://github.com/TU_USUARIO/ALP-Discretas1
  cd analizador-logico
```
2. **Ejecutar el programa en la terminal**
```
  python main.py
```
3. **Ingresar una fórmula en LaTeX sin paréntesis**, por ejemplo:
```
  \neg p \rightarrow q \wedge r
```
4. **Recibirás como salida la misma fórmula bien parentizada**, según la jerarquía de operadores definida.

---

## Manual de uso completo

Para más detalles sobre las fórmulas permitidas, ejemplos, añadir operandos validos, edición de jerarquía y errores posibles, consulta el manual completo disponible en este repositorio:

- [`docs/Manual_de_uso.pdf`](docs/Manual_de_uso.pdf)

Este documento incluye:

- Tipos de entrada válidos
- Reglas de sintaxis esperadas
- Ejemplos funcionales de entrada y salida
- Cómo añadir operandos válidos
- Cómo editar la jerarquía en `tabla.csv`
- Manejo de errores comunes como uso incorrecto de `\neg`

---

## Personalización

### Operandos válidos

Actualmente se admiten como operandos las letras `p`, `q`, `r`. Para aceptar más variables, edita `logic/tokenizer.py`: como lo indica la sección "Añadir operandos" en el [Manual](docs/Manual_de_uso.pdf).



### Jerarquía de operadores

El archivo `data/tabla.csv` permite redefinir la relación de precedencia (`>, <, =`) entre conectivos lógicos. Para más información, consulta la sección “Manejo de jerarquía” en el [Manual](docs/Manual_de_uso.pdf).

---

## Ejecución de pruebas

El proyecto incluye pruebas unitarias (basadas en `unittest`). Para ejecutarlas:
```
python -m unittest discover tests
```
---

## Licencia

Este proyecto está bajo la [Licencia MIT](https://opensource.org/licenses/MIT). Puedes usarlo, modificarlo y distribuirlo libremente.

---

## Autores

**Brandon Losada**  
Universidad Nacional de Colombia

**Luis Miguel Sanchez**  
Universidad Nacional de Colombia

---

## Contribuciones

Contribuciones y mejoras son bienvenidas. Si deseas colaborar:

1. Haz un fork del proyecto
2. Crea una nueva rama con tu mejora
3. Abre un pull request explicando claramente los cambios

---
