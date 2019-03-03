var io = require('socket.io')(8002);
io.on('connection', function (socket) {
    socket.on('room', function(data) { 
        socket.join(data); 
    })
    socket.on('Send_EmmitTicket', function (data) {
        io.sockets.in(data.company).emit('Recibe_EmmitTicket', data);
    });
    socket.on('Send_PrintTicket', function (data) {
        io.sockets.in(data.company).emit('Recibe_PrintTicket', data);
    });
    //socket.on('payment_ticket', function (data) {
        //io.sockets.in(data.company).emit('payment_ticket', data);
    //});
    //socket.on('print_cut', function (data) {
        //io.sockets.in(data.company).emit('cordova_cut', data);
    //});
    //socket.on('payment_ticket', function (data) {
        //io.sockets.in(data.company).emit('payment_ticket', data);
    //});
    //socket.on('reload', function (data) {
        //io.sockets.in(data.company).emit('reload');
    //});
    //socket.on('update_products', function (data) {
        //io.sockets.in(data.company).emit('update_products');
    //});
    //socket.on('printer_connected', function (data) {
        //io.sockets.in(data.company).emit('printer_connected', data);
    //});
});
