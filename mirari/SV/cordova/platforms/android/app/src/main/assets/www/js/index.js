var app = {
    initialize: function() {
        document.addEventListener('deviceready', this.onDeviceReady.bind(this), false);
    },
    onDeviceReady: function() {
        new Vue({
            el: '#app',
            data: {
                REINICIAR: 'CLICK PARA REINICIAR APLICACIÓN',
                PublicSocket: null,
                variables:{
                    organizationCode: "TAHONA",
                    sellpoint: "SUSY CAJA",
                    port: "8086",
                    isServer: false,
                    model: 'TSP100',
                },
                ip: null,
            },
            created:function(){
                self = this
            },
            mounted: function () {
                function ipSuccess( ipInformation ) {
                    self.ip = ipInformation.ip
                }
                networkinterface.getWiFiIPAddress( ipSuccess );
                alert(self.ip)
                //self.PublicSocket = io('http://50.18.229.242:8002')
                //self.PublicSocket.emit('room', 'TAHONA');
                //var ref = cordova.InAppBrowser.open('http://tahona.tahona.mx', '_blank', 'location=no,toolbar=no,zoom=no,presentationstyle=fullscreen');
                //let PrinterConection = () => {
                    //PublicSocket.emit('Send_Event', self.variables.organizationCode, 'printerConection', {
                        //url: 'http://'+ip.address().toString()+':'+self.variables.port.toString(),
                        //name: self.variables.sellpoint,
                        //organizationCode: self.variables.organizationCode,
                    //});
                //};
            },
            methods: {
                reload() {
                    location.reload();
                },
            },
        });
        
    },
};
app.initialize();