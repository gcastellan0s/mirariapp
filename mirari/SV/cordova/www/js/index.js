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
                let ipSuccess = (ipInformation) => {
                    self.ip = ipInformation
                }
                networkinterface.getWiFiIPAddress( ipSuccess );
                self.PublicSocket = io('http://50.18.229.242:8002')
                self.PublicSocket.emit('room', self.variables.organizationCode);
                let PrinterConection = () => {
                    self.PublicSocket.emit('Send_Event', self.variables.organizationCode, 'printerConection', {
                        url: 'http://'+self.ip+':'+self.variables.port,
                        name: self.variables.sellpoint,
                        organizationCode: self.variables.organizationCode,
                    });
                };
                //var ref = cordova.InAppBrowser.open('http://tahona.tahona.mx', '_blank', 'location=no,toolbar=no,zoom=no,presentationstyle=fullscreen');
                PrinterConection();
                setInterval(function(){
                    PrinterConection();
                }, 60000);
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