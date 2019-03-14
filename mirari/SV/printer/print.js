'use strict';
const variables = require('./variables');
const {PythonShell} = require("python-shell");
const ip = require('ip');

var PublicSocket = require('socket.io-client')('ws://50.18.229.242:8002');
PublicSocket.emit('room', variables.organizationCode);

var data = {
    url: 'ws://'+ip.address().toString()+':'+variables.port.toString(),
    name: variables.sellpoint,
    organizationCode: variables.organizationCode,
    isServer: variables.isServer
}

let PrinterConection = () => {
    PublicSocket.emit('Send_Event', variables.organizationCode, 'PrinterConection', data);
};

PrinterConection();
setInterval(function(){
    PrinterConection();
}, 15000);

var io = require('socket.io')(variables.port);
io.on('connection', function (socket) {
    socket.on('Send_Event', function(organizationCode, event, data) {
        if (event == 'Print'){
            var pyshell = new PythonShell('pyprint.py', {
                mode: 'json',
                pythonPath: '/usr/bin/python3',
                scriptPath: '/home/pi/printer',
            });
            pyshell.send(data).end(function (err) {
                if (err){
                    console.log(err)
                    return 0;
                }
            });
        }
    });
});
