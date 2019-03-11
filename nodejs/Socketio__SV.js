var io = require('socket.io')(8002);
io.on('connection', function (socket) {
    socket.on('room', function(data) { 
        socket.join(data); 
    })
    socket.on('Send_Event', function (organizationCode, event, data) {
        console.log(event)
        io.sockets.in(organizationCode).emit('Recibe_Event', event, data);
    });
});
