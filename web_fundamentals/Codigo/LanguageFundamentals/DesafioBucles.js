function printImpar1a20(){
    console.log("Impares del 1 al 20");
    for(var i=1;i<=20;i++){
        if(i%2!=0){
            console.log(i);
        }
    }
}

function multiplosDe3(){
    console.log("Multiplos de 3 del 100 al 0");
    for (var i=100; i>=0;i--){
        if(i%3==0){
            console.log(i);
        }
    }
}

function secuencia(){
    console.log("Secuencia")
    var num=4;
    while(num>=-3.5){
        console.log(num);
        num-=1.5
    }
}

function sigma(){
    var num=0;
    for(var i=1;i<=100;i++){
        num+=i;
    }
    console.log("Sigma")
    console.log(num)
}

function factorial(){
    var num=1;
    for(var i=1;i<=12;i++){
        num*=i;
    }
    console.log("Factorial")
    console.log(num)
}

printImpar1a20();
multiplosDe3();
secuencia();
sigma();
factorial();