import re

def validar_fen(fen):
    partes = fen.strip().split()

    if len(partes) != 6:
        return False, "La FEN debe tener exactamente 6 campos"

    tablero, turno, enroque, passant, halfmove, fullmove = partes

    filas = tablero.split('/')

    if len(filas) != 8:
        return False, "El tablero debe tener 8 filas"

    piezas_validas = "pnbrqkPNBRQK"

    for fila in filas:
        suma = 0

        for char in fila:
            if char.isdigit():
                suma += int(char)
            elif char in piezas_validas:
                suma += 1
            else:
                return False, f"Carácter inválido en tablero: {char}"

        if suma != 8:
            return False, "Cada fila del tablero debe sumar 8 casillas"

    if turno not in ['w', 'b']:
        return False, "Turno inválido"

    if not re.fullmatch(r'-|[KQkq]+', enroque):
        return False, "Enroque inválido"

    if not re.fullmatch(r'-|[a-h][36]', passant):
        return False, "En passant inválido"

    if not halfmove.isdigit():
        return False, "Halfmove debe ser entero"

    if not fullmove.isdigit() or int(fullmove) < 1:
        return False, "Fullmove debe ser entero mayor o igual a 1"

    return True, "FEN válida"


fen = input("Ingrese cadena FEN: ")

valida, mensaje = validar_fen(fen)

print(mensaje)