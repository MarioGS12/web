document.addEventListener('DOMContentLoaded', () => {

 var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    var room_1 = "sala01";


    document.querySelector('#room01').onsubmit = () => {


        const mensaje= document.querySelector('#mensaje-room').value;

        socket.emit('sala01', {'chat': mensaje,'room': room_1});

        document.querySelector('#mensaje-room').value="";
        return false;


    };


 socket.on('sala01 respuesta', data => {
        const li = document.createElement('li');
        li.innerHTML =data["chat"];
        document.querySelector('#chatroom').append(li);

     });




});