'use strict';
const variables = require('./variables');
const {PythonShell} = require("python-shell");

var ip = require('ip');
var socket_client = require('socket.io-client')(variables.domain);

socket_client.emit('room', variables.code);
socket_client.emit('printer_connected',{'company':variables.code,'port':variables.port,'name':variables.name,'ip':ip.address(),'url':'http://'+ip.address().toString()+':'+variables.port.toString()});

setInterval(function(){
	socket_client.emit('printer_connected',{'company':variables.code,'port':variables.port,'name':variables.name,'ip':ip.address(),'url':'http://'+ip.address().toString()+':'+variables.port.toString()});
}, 10000);

var io = require('socket.io')(variables.port);
io.on('connection', function (socket) {
	socket.on('print_ticket', function(data) {
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
	socket.on('make_cut', function (data) {
		var pyshell = new PythonShell('make_cut.py', {
			mode: 'json',
			pythonPath: '/usr/bin/python3',
			scriptPath: '/home/pi/mirari-printer',
		});
		pyshell.send(data).end(function (err) {
			if (err) {
				console.log(err)
				return 0;
			}
		});
	});
});
