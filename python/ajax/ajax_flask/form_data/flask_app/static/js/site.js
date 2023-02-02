
$(document).ready(
    function(){

        var myForm = document.getElementById('myForm')
        myForm.onsubmit = function(e){
            // "e" es el evento JS que ocurre cuando enviamos el formulario
            // e.preventDefault() es un método que detiene la naturaleza predeterminada de JavaScript
            e.preventDefault();
            // crea el objeto FormData desde JavaScript y envíalo a través de una solicitud post fetch
            var form = new FormData(myForm);
            // así es como configuramos una solicitud post y enviamos los datos del formulario
            fetch("http://127.0.0.1:5000/create/user", { method :'POST', body : form})
                .then( response => response.json() )
                .then( data =>{
                    console.log(data) 
                    console.log(data.data)
                    console.log(data.data.email)
                    var users = document.getElementById('users');
                    let row = document.createElement('tr');
                    let name = document.createElement('td');
                    name.innerHTML = data.data.user_name;
                    row.appendChild(name);
                    
                    let email = document.createElement('td');
                    email.innerHTML = data.data.email;
                    row.appendChild(email);
                    users.appendChild(row);

                    console.log(document.getElementById("name"));
                    document.getElementById("name").value = "";
                    document.getElementById("email").value = "";
                })
    }
    getUsers();
});



function getUsers(){
    console.log("user get")
    fetch('http://127.0.0.1:5000/users')
        .then(res =>  res.json())
        .then(data => {
            var users = document.getElementById('users');
            for( let i = 0; i < data.length; i++){
                let row = document.createElement('tr');

                let name = document.createElement('td');
                name.innerHTML = data[i].user_name;
                row.appendChild(name);
                
                let email = document.createElement('td');
                email.innerHTML = data[i].email;
                row.appendChild(email);
                users.appendChild(row);
            }
        })

}