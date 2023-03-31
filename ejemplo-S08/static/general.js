document.addEventListener('DOMContentLoaded', () => {

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    var room_1 = "sala01";

    document.querySelector('#chat01').onsubmit = () => {



        const mensaje= document.querySelector('#mensaje').value;

        socket.emit('general', {'chat': mensaje,'room': room_1});

        document.querySelector('#mensaje').value="";
        return false;
    };

    socket.on('general respuesta', data => {
        const li = document.createElement('li');
        li.innerHTML =data["chat"];
        document.querySelector('#chat').append(li);

     });

});