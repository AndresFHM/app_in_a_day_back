import fetch from 'node-fetch';
let recipes;

fetch('http://127.0.0.1:5000')
    .then((response) => response.json())
    .then((data) => {
        console.log(data)
    });
