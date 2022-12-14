function eliminar(element){
    element.remove();
}

function alerta(){
    var element = document.querySelector(".search");
    if (element.value!=""){
        alert('You are searching for "'+element.value+'"');
    }
}

function aumentar(element){
    console.log(element.innerText);
    var num = parseInt(element.innerText);
    num++;
    element.innerText = num;
}