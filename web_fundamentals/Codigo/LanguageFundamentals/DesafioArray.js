function alwaysHungry(arr) {
    var hambriento = true;
    for (var i=0; i<arr.length;i++){
        if(arr[i]=="comida"){
            console.log("delicioso");
            hambriento=false;
        }
    }
    if(hambriento){
        console.log("Tengo hambre");
    }
    // tu código aquí 
}
function highPass(arr, cutoff) {
    var filteredArr = [];
    for(var i=0; i<arr.length;i++){
        if(arr[i]>cutoff){
            filteredArr.push(arr[i])
        }
    }
    return filteredArr;
}

function betterThanAverage(arr) {
    var sum = 0;
    for(var i=0;i<arr.length;i++){
        sum+=arr[i];
    }
    sum/=arr.length;
    var count = 0
    for(var i=0;i<arr.length;i++){
        if(arr[i]>sum){
            count++;
        }
    }
    return count;
}

function reverse(arr) {
    var aux = "";
    var j=0;
    for(var i=arr.length-1; i>arr.length/2; i--){
        aux = arr[i];
        arr[i]=arr[j];
        arr[j]=aux;
        j++;
    }
    return arr;
}

function fibonacciArray(n) {
    // [0, 1] son los valores inciales del arreglos para calcular el resto
    var fibArr = [0, 1];
    var sum = 0;
    for(var i=1; i<n-1; i++){
        sum=fibArr[i]+fibArr[i-1];
        fibArr.push(sum);
    }
    return fibArr;
}


 
alwaysHungry([3.14, "comida", "pastel", true, "comida"]);
// esto debería mostrar "delicioso, "delicioso"
alwaysHungry([4, 1, 5, 7, 2]);
// esto debería mostrar "Tengo hambre"

var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); // esperamos de vuelta [6, 8, 10, 9]

var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // esperamos 4 de vuelta

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // esperamos de vuelta ["e", "d", "c", "b", "a"]

var result = fibonacciArray(10);
console.log(result); // esperamos de vuelta[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
