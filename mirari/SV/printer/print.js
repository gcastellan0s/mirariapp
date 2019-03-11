'use strict';
const variables = require('./variables');
const {PythonShell} = require("python-shell");
const io = require('socket.io')
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
	PublicSocket.emit('Send_PrinterConection', variables.organizationCode, data);
};

PrinterConection();
setInterval(function(){
	PrinterConection();
}, 15000);

var io = require('socket.io')(variables.port);
io.on('connection', function (socket) {
	socket.on('Recibe_PrintTicket', function(data) {
		var pyshell = new PythonShell('print_ticket.py', {
			mode: 'json',
			pythonPath: '/usr/bin/python3',
			scriptPath: '/home/pi/mirari-printer',
		});
		pyshell.send(data).end(function (err) {
			if (err){
				console.log(err)
				return 0;
			}
		});
	});
	//socket.on('make_cut', function (data) {
		//var pyshell = new PythonShell('make_cut.py', {
			//mode: 'json',
			//pythonPath: '/usr/bin/python3',
			//scriptPath: '/home/pi/mirari-printer',
		//});
		//pyshell.send(data).end(function (err) {
			//if (err) {
				//console.log(err)
				//return 0;
			//}
		//});
	//});
});
