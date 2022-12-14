
function like(num){
    var string = ""
    string = ".cont_"+num;
    var cont =parseInt(document.querySelector(string).innerText);
    cont++;
    document.querySelector(string).innerText=cont;
}