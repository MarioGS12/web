// Connect to websocket
var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

// When connected, configure buttons
socket.on('connect', () => {

    // Each button should emit a "submit vote" event
    document.querySelectorAll('button.options').forEach(button => {
        button.onclick = () => {
            const selection = button.dataset.vote;
            let question = document.getElementById("question-name").innerHTML;
            socket.emit('submit vote', {'selection': selection, 'question': question});
        };
    });
    socket.emit("cargar preguntas",{});
});

// When a new vote is announced, add to the unordered list
socket.on('vote totals', data => {
    document.querySelector('#yes').innerHTML = data.yes;
    document.querySelector('#no').innerHTML = data.no;
    document.querySelector('#maybe').innerHTML = data.maybe;
});

socket.on('cargar votos', data => {
    document.querySelector('#yes').innerHTML = data.yes;
    document.querySelector('#no').innerHTML = data.no;
    document.querySelector('#maybe').innerHTML = data.maybe;
});

const agregarPregunta = () => {
    let pregunta = document.querySelector("#pregunta").value;
    socket.emit('agregar pregunta', {'pregunta': pregunta});
}
var template = Handlebars.compile(`<li onclick="votar('{{content}}')" >{{content}}</li>`)

socket.on("pregunta nueva", (data)=>{
    if(data.error){
        alert(data.error)
    }else{
        document.querySelector("#pregunta").value = "";
        document.querySelector(".lista-preguntas").innerHTML += template({'content': data.pregunta});

    }
})

socket.on("cargar preguntas", (data)=>{

    data.preguntas.forEach(pregunta =>{
        document.querySelector(".lista-preguntas").innerHTML +=  template({'content': pregunta});;
    })

})
const votar = (pregunta) =>{
    document.getElementById("question-name").innerHTML = pregunta;
    socket.emit("cargar votos", {'pregunta': pregunta})

}