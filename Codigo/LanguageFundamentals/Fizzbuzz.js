function fizzBuzz(){
    var str = "";
    for (var i=1;i<=100;i++){
        if(i%3==0){
            str+="Fizz";
        }
        if(i%5==0){
            str+="Buzz";
        }
        if((i%5==0)||(i%3==0)){
            console.log(str);
        }
        else{
            console.log(i);
        }
        str=""
    }
}


fizzBuzz();