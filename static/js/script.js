window.addEventListener('load', start);

let firstname = document.querySelector('#firstname');
let lastname = document.querySelector('#lastname');
let dob = document.querySelector('#dob');

function preventFormSubmit() {
    function handleFormSubmit(event) {
        event.preventDefault(); //função para evitar o submit
        sendJSON();
    }
  
    //captura o elemento form
    var form = document.querySelector('form');
    //verifica o evento submit, e executa a função handle...
    form.addEventListener('submit', handleFormSubmit);
  }

function sendJSON(){

    // Creating a XHR object
    let xhr = new XMLHttpRequest();
    let url = "http://127.0.0.1:8000/cadastro/";

    // open a connection
    xhr.open("POST", url, true);

    // Set the request header i.e. which type of content you are sending
    xhr.setRequestHeader("Content-Type", "application/json");
    
    // Converting JSON data to string
    var data = JSON.stringify({
    "firstname": firstname.value,
    "lastname": lastname.value,
        "dob": dob.value});

    // Sending data with the request
    console.log(data);
    xhr.send(data);
}

function start() {
    console.log("Carregado");
    preventFormSubmit();
}