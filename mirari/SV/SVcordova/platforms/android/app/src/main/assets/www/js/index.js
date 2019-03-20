var app = {
    initialize: function() {
        document.addEventListener('deviceready', this.onDeviceReady.bind(this), false);
    },
    onDeviceReady: function() {
        var ref = cordova.InAppBrowser.open('http://tahona.tahona.mx/', '_blank', 'location=no,toolbar=no,zoom=no,presentationstyle=fullscreen');
    },
};
app.initialize();