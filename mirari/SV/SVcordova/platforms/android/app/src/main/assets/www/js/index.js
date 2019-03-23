var app = {
    initialize: function() {
        document.addEventListener('deviceready', this.onDeviceReady.bind(this), false);
    },
    onDeviceReady: function() {
        new Vue({
            el: '#app',
            data: {
                REINICIAR: 'CLICK PARA REINICIAR APLICACIÓN',
            },
            created:function(){
                self = this
            },
            mounted: function () {
                window.addEventListener("batterystatus", onBatteryStatus, false);
                function onBatteryStatus(status) {
                    console.log("Level: " + status.level + " isPlugged: " + status.isPlugged);
                }
                navigator.notification.beep(2);
                var ref = cordova.InAppBrowser.open('http://tahona.tahona.mx', '_blank', 'location=no,toolbar=no,zoom=no,presentationstyle=fullscreen');
            },
            methods: {
                reload() {
                    console.log('reiniciando')
                    location.reload();
                },
            },
        });
        
    },
};
app.initialize();

