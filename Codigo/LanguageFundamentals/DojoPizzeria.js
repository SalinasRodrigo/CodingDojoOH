function sandwichFactory(pan, proteina, queso, salsas) {
    var sandwich = {};
    sandwich.pan = pan;
    sandwich.proteina = proteina;
    sandwich.queso = queso;
    sandwich.salsas = salsas;
    return sandwich;
}
    
var s1 = sandwichFactory("trigo", "pavo", "provolone", ["mostaza", "cebolla frita", "rúcula"]);
console.log(s1);
var s2 = sandwichFactory("estilo Chicago", ["peperoni", "salchicha"], ["mozarella"], "tradicional");
console.log(s2);
var s3 = sandwichFactory("lazada a mano", "marinara", ["mozzarella", "feta"], ["champiñones", "aceitunas", "cebollas"]);
console.log(s3);
var s4 = sandwichFactory("lazada a mano",  ["peperoni", "salchicha"], "provolone", ["champiñones", "aceitunas", "cebollas"]);
console.log(s4);
var s5 = sandwichFactory("trigo", "marinara", ["mozzarella", "feta"], ["mostaza", "cebolla frita", "rúcula"]);
console.log(s5);