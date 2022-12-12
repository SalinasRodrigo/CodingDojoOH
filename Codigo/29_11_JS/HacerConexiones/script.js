

function solicitud(num){
    if(num<0){
        num*=-1;
    }
    else{
        var cont2=parseInt(document.querySelector(".numero_conexiones").innerText);
        cont2++;
        document.querySelector(".numero_conexiones").innerText=cont2;
    }
    var string = "solicitud_"+num;
    document.getElementById(string).remove();
    var cont=parseInt(document.querySelector(".numero_solicitudes").innerText); 
    cont--;
    document.querySelector(".numero_solicitudes").innerText=cont;
}

function editar(){
    document.querySelector(".info h1").innerText="Janne Doe";
}
