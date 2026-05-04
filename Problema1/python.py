import time
import os


# Genera los coeficientes de (x+1)^n usando el Triángulo de Pascal
def generar_coeficientes(n):
    fila = [1]

    for i in range(n):
        nueva = [1]

        for j in range(len(fila) - 1):
            nueva.append(fila[j] + fila[j + 1])

        nueva.append(1)
        fila = nueva

    return fila


# Construye la representación textual del polinomio
def construir_polinomio(coef):
    n = len(coef) - 1
    terminos = []

    for i, c in enumerate(coef):
        exp = n - i

        if exp > 1:
            terminos.append(f"{c}x^{exp}" if c != 1 else f"x^{exp}")
        elif exp == 1:
            terminos.append(f"{c}x" if c != 1 else "x")
        else:
            terminos.append(str(c))

    return " + ".join(terminos)


# Evalúa el polinomio término por término mostrando el procedimiento
def evaluar_pasos(coef, x):
    n = len(coef) - 1
    total = 0
    pasos = []

    print("\nEvaluacion paso a paso:")

    for i, c in enumerate(coef):
        exp = n - i
        termino = c * (x ** exp)
        total += termino

        paso = f"{c} * {x}^{exp} = {termino}"
        pasos.append(paso)

        print(paso)

    print(f"\nResultado final: {total}")

    return pasos, total


# Captura de datos ingresados por el usuario
n = int(input("Ingrese n: "))
x = int(input("Ingrese x: "))

# Inicio de medición del tiempo de ejecución
inicio = time.perf_counter()

coeficientes = generar_coeficientes(n)
polinomio = construir_polinomio(coeficientes)
pasos, resultado = evaluar_pasos(coeficientes, x)

# Fin de medición del tiempo
fin = time.perf_counter()

print("\nCoeficientes:", coeficientes)
print("Polinomio:", polinomio)
print(f"Tiempo ejecución: {fin - inicio:.10f} segundos")

# Genera la ruta del archivo en el mismo directorio del script
ruta = os.path.join(os.path.dirname(__file__), "resultadoPython.txt")

# Escritura de resultados en archivo de salida
with open(ruta, "w") as f:
    f.write(f"n = {n}\n")
    f.write(f"x = {x}\n\n")
    f.write(f"Coeficientes: {coeficientes}\n")
    f.write(f"Polinomio: {polinomio}\n\n")
    f.write("Evaluacion paso a paso:\n")

    for paso in pasos:
        f.write(paso + "\n")

    f.write(f"\nResultado final: {resultado}\n")
    f.write(f"Tiempo ejecucion: {fin - inicio:.10f} segundos\n")