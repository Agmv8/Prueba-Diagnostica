import re

reservadas_c = {
    "int": "entero",
    "float": "flotante",
    "char": "carácter",
    "if": "si",
    "else": "sino",
    "for": "para",
    "while": "mientras",
    "return": "retornar"
}

codigo = input("Ingrese código en C: ")

tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', codigo)

for token in tokens:
    if token in reservadas_c:
        print(f"{token} → {reservadas_c[token]}")