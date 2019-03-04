"use strict";
var io = require('socket.io')(8002);
io.on('connection', function (socket) {
    socket.on('room', function(data) { 
        socket.join(data); 
    })
    //socket.on('Send_EmmitTicket', function (organizationId, data) {
        //io.sockets.in(organizationId).emit('Recibe_EmmitTicket', data);
    //});
    socket.on('Send_PrintTicket', function (organizationId, data) {
        io.sockets.in(organizationId).emit('Recibe_PrintTicket', data);
    });
});
