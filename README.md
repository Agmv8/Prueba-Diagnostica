# Prueba Diagnóstica – Lenguajes y Compiladores

## Autor

Alondra Moreno 

---

## Descripción del Proyecto

Este repositorio contiene la solución de la prueba diagnóstica de la asignatura **Lenguajes y Compiladores**, desarrollada en **Python** y **JavaScript**.

Se implementaron tres problemas aplicando estructuras dinámicas, validación sintáctica y análisis léxico básico.

---

## Lenguajes Utilizados

* Python 3
* JavaScript (Node.js)

---

## Problemas Desarrollados

### Problema 1 – Desarrollo de ((x+1)^n)

Generación dinámica de los coeficientes del polinomio utilizando el **Triángulo de Pascal**, construcción de la expresión algebraica, evaluación paso a paso para un valor de `x` y medición del tiempo de ejecución.

#### Funcionalidades

* Generación dinámica de coeficientes binomiales
* Construcción textual del polinomio
* Evaluación paso a paso
* Medición de tiempo de ejecución
* Exportación de resultados a archivo `.txt`

---

### Problema 2 – Validación de Notación FEN

Validación sintáctica de cadenas en formato **Forsyth–Edwards Notation (FEN)** para posiciones de ajedrez.

#### Validaciones Implementadas

* Estructura de 6 campos
* 8 filas en el tablero
* 8 casillas por fila
* Piezas válidas
* Turno activo válido
* Enroque válido
* En passant válido
* Halfmove y Fullmove correctos

---

### Problema 3 – Traducción de Palabras Reservadas de C

Análisis léxico básico para identificar palabras reservadas de código fuente en lenguaje C y traducirlas al español.

#### Funcionalidades

* Tokenización de código fuente
* Detección de palabras reservadas
* Traducción al español
* Simulación básica de análisis léxico

---

## Estructura del Proyecto

```bash
/Proyecto
│
├── problema1_python.py
├── problema1_javascript.js
│
├── problema2_python.py
│
├── problema3_python.py
│
├── resultadoPython.txt
├── resultado_javascript.txt
│
└── README.md
```

---

## Cómo Ejecutar

### Python

```bash
python nombre_archivo.py
```

### JavaScript

```bash
node nombre_archivo.js
```

---

## Complejidad Computacional

| Problema   | Complejidad |
| ---------- | ----------- |
| Problema 1 | O(n²)       |
| Problema 2 | O(n)        |
| Problema 3 | O(n)        |

---

## Conceptos de Compiladores Aplicados

* **Memoria dinámica**
* **Tokenización**
* **Análisis léxico**
* **Validación sintáctica**
* **Procesamiento de cadenas**
* **Expresiones regulares**

---

## Observaciones

* Se mantuvo la misma lógica algorítmica en Python y JavaScript para permitir comparación de rendimiento.
* Los programas fueron diseñados para ejecutarse desde consola.
* El Problema 1 genera archivos de salida automáticamente con los resultados obtenidos.

---

## Conclusión

El proyecto demuestra la aplicación práctica de conceptos fundamentales de programación y compiladores mediante la implementación de algoritmos de generación combinatoria, validación sintáctica y análisis léxico básico en dos lenguajes distintos.

---
Link de la Defensa