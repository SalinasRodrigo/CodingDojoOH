var num=['',''];
var op='';
var i = 0;

function press(numint){
    num[i]+=numint;
    console.log(num[i]);
    $("#display").text(num[i]);
}
function clr(){
    res=0;
    $("#display").text(0);
}
function setOP(sim){
    op=sim;
    if(i==1){
        num[0]='';
        i=0;
    }
    else{
        num[1]='';
        i=1;
    }
    $("#display").text(0);
}
function calculate(){
    console.log(num);
    if(op=='+'){
        $("#display").text(parseFloat(num[0])+parseFloat(num[1]));
    }
    if(op=='-'){
        $("#display").text(parseFloat(num[0])-parseFloat(num[1]));
    }
    if(op=='*'){
        $("#display").text(parseFloat(num[0])*parseFloat(num[1]));
    }
    if(op=='/'){
        $("#display").text(parseFloat(num[0])/parseFloat(num[1]));
    }
    i=0;
    num[1]='';
    num[0]='';
    op='';
}