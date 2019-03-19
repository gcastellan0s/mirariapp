var app = {
    initialize: function() {
        document.addEventListener('deviceready', this.onDeviceReady.bind(this), false);
    },
    onDeviceReady: function() {
        var socket = io('ws://50.18.229.242:8002')
        socket.emit('room', 'tahona');
        var ref = cordova.InAppBrowser.open('http://tahona.mx/', '_blank', 'location=no,toolbar=no,zoom=no,presentationstyle=fullscreen');
    },
};
app.initialize();