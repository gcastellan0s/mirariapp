var io = require('socket.io')(8002);

io.on('connection', function (socket) {
    socket.on('room', function(data) { 
        socket.join(data); 
    })
    socket.on('Send_PrintTicket', function (organizationCode, data) {
        io.sockets.in(organizationCode).emit('Recibe_PrintTicket', data);
    });
    socket.on('Send_PrinterConection', function (organizationCode, data) {
        io.sockets.in(organizationCode).emit('Recibe_PrinterConection', data);
    });
    socket.on('Send_TicketPayment', function (organizationCode, data) {
        io.sockets.in(organizationCode).emit('Recibe_TicketPayment', data);
    });
});