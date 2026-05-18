//constante
const pi = 3.141592653589793;

//operadores

console.log (1 + 1);
console.log (1 - 1);
console.log (6 * 6);
console.log (12 / 2);

//comparativo

console.log (4 == 4);
console.log (4 == 41);
console.log (4 == "4");
console.log (4 === "4");

//condicionales

let autorizado = true;

if (autorizado) {
    console.log ("Puede pasar");
} else{
    console.log ("acceso denegado");
}

let autorizado2 = false;

if (autorizado2) {
    console.log ("Puede pasar");
} else{
    console.log ("acceso denegado");
}

//funciones

function sumar(primero, segundo) {
    return primero + segundo;
}

let resultado = sumar(7,5);
console.log (resultado);

//multiplicacion
function multiplicacion(primero, segundo) {
    return primero * segundo;
}

let resultado2 = multiplicacion(5,5);
console.log (resultado2);