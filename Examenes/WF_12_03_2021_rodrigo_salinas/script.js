/**
 * Función para eliminar el bloque de suscripción, busca
 * el elemento ".sucribe_blcok" con la función querySelector y 
 * la elimina con la función remove.
 */
function eliminar(){
    var element = document.querySelector(".sucribe_blcok")
    element.remove();
}

/**
 * La función aumentar recibe como parametro un elemento 
 * busca el texto asociado a este y lo convierte a entero,
 * este entero sera un contador que aumentara y sobreescribira
 * el texto anterior del elemento.
 */
function aumentar(element){
    var cont = parseInt(element.innerText);
    cont++;
    element.innerText=cont;
}
/**
 * Esta función mostra el ganador entre los dos equipos que se encuentran
 * disputando en el bloque principal, en base al valor entero de los 
 * puntajes de estos (".score_1" y ".score_2") lanzara una alerta con el nombre
 * del equipo ganador.
 */
function ganador(){
    var score1 = parseInt(document.querySelector(".score_1").innerText);
    var score2 = parseInt(document.querySelector(".score_2").innerText);
    if(score1<score2){
        alert("The "+document.querySelector(".name_2").innerText+" have won!");
    }else{
        alert("The "+document.querySelector(".name_1").innerText+" have won!");
    }
    
}
/**
 * La función ganador se activa tras 13 segundo (13000 milisegundos)
 * definidos en el setTimeout.
 */
function actualizarTiempo(timerInt){
    var element = document.querySelector(".timer");
    element.innerText="0:"+timerInt;
    return timerInt--;
}
window.onload = function (){
    setTimeout(ganador, 13000);
}