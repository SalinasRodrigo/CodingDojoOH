$("document").ready(function(){
   getInfo();
  });

function removeCookie(){
    $("#cookie").remove();  
}

async function getInfo(){
    var response = await fetch("http://api.openweathermap.org/data/2.5/forecast/daily?id=524901&APPID=fc8d82bbb92cf9df3df411fd4ca85f79")
    var coderData = await response.json();
    console.log(coderData)
}



function cambioMdedida(medida){
    console.log(medida.value)
    if(medida.value=="ºF"){
        for(i=1;i<=4;i++){
            var maxima = document.querySelector("#dia_"+i+" .maxima");
            var minima = document.querySelector("#dia_"+i+" .minima");
            celciusFahrenheit(maxima);
            celciusFahrenheit(minima);
        }
    }else{
        for(i=1;i<=4;i++){
            var maxima = document.querySelector("#dia_"+i+" .maxima");
            var minima = document.querySelector("#dia_"+i+" .minima");
            fahrenheitCelcius(maxima);
            fahrenheitCelcius(minima);
        }
    }
    
}

function celciusFahrenheit(temp){
    var str = temp.innerText;
    str = str.replace('º','');
    var tempInt = parseInt(str);
    tempInt = (tempInt*(9/5)) + 32;
    tempInt=tempInt.toFixed(0)
    temp.innerText = tempInt+"º";
    
}

function fahrenheitCelcius(temp){
    var str = temp.innerText;
    str = str.replace('º','');
    var tempInt = parseInt(str);
    tempInt = (tempInt-32)/1.8;
    tempInt=tempInt.toFixed(0)
    temp.innerText = tempInt+"º"; 
}
