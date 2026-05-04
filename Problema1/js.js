const fs = require("fs");
const readline = require("readline");

// Genera la fila n del Triángulo de Pascal dinámicamente
function generarCoeficientes(n) {
    let fila = [1];

    for (let i = 0; i < n; i++) {
        let nueva = [1];

        for (let j = 0; j < fila.length - 1; j++) {
            nueva.push(fila[j] + fila[j + 1]);
        }

        nueva.push(1);
        fila = nueva;
    }

    return fila;
}

// Construye el polinomio en formato legible a partir de los coeficientes
function construirPolinomio(coef) {
    let n = coef.length - 1;

    return coef.map((c, i) => {
        let exp = n - i;

        if (exp > 1) return c === 1 ? `x^${exp}` : `${c}x^${exp}`;
        if (exp === 1) return c === 1 ? `x` : `${c}x`;
        return `${c}`;
    }).join(" + ");
}

// Evalúa el polinomio término por término mostrando el procedimiento
function evaluarPasos(coef, x) {
    let n = coef.length - 1;
    let total = 0;
    let pasos = [];

    console.log("\nEvaluación paso a paso:");

    coef.forEach((c, i) => {
        let exp = n - i;
        let termino = c * (x ** exp);
        total += termino;

        let paso = `${c} * ${x}^${exp} = ${termino}`;
        pasos.push(paso);

        console.log(paso);
    });

    console.log(`\nResultado final: ${total}`);

    return { pasos, total };
}

// Interfaz para capturar datos por consola
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Ingrese n: ", (nInput) => {
    rl.question("Ingrese x: ", (xInput) => {

        const n = parseInt(nInput);
        const x = parseInt(xInput);

        // Inicio medición de tiempo de ejecución
        const inicio = performance.now();

        const coeficientes = generarCoeficientes(n);
        const polinomio = construirPolinomio(coeficientes);
        const evaluacion = evaluarPasos(coeficientes, x);

        // Fin medición de tiempo
        const fin = performance.now();

        console.log("\nCoeficientes:", coeficientes);
        console.log("Polinomio:", polinomio);
        console.log(`Tiempo ejecución: ${(fin - inicio).toFixed(10)} ms`);

        // Preparación del contenido para archivo de salida
        let contenido = `n = ${n}\n`;
        contenido += `x = ${x}\n\n`;
        contenido += `Coeficientes: ${coeficientes}\n`;
        contenido += `Polinomio: ${polinomio}\n\n`;
        contenido += `Evaluación paso a paso:\n`;

        evaluacion.pasos.forEach(paso => {
            contenido += paso + "\n";
        });

        contenido += `\nResultado final: ${evaluacion.total}\n`;
        contenido += `Tiempo ejecución: ${(fin - inicio).toFixed(10)} ms`;

        // Escritura de resultados en archivo txt
        fs.writeFileSync("resultado_javascript.txt", contenido);

        rl.close();
    });
});