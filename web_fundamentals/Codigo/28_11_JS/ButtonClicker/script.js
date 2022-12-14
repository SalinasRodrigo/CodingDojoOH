function login_logout(element) {
    //Si el texto es Logout al clickear pasara a ser
    //Login
    if(element.innerText=="Logout"){
        element.innerText="Login";
        return;
    }
    //si no lo es significa que es un login asi que pasara a ser
    //un logout
    element.innerText = "Logout";
}

function hide(element) {
    console.log(element);
    element.remove();
    
}



function likes() {
    var clicks = parseInt(document.getElementById("contador").innerHTML);
    clicks += 1;
    document.getElementById("contador").innerHTML = clicks;
};
