var app = {
    initialize: function() {document.addEventListener('deviceready', this.onDeviceReady.bind(this), false)},
    onDeviceReady: function() {
        const router = new VueRouter({routes:[{ path:'/',component:{template:``}}]});
        const ax = axios.create({
            xsrfCookieName: 'csrftoken',
            xsrfHeaderName: 'X-CSRFToken',
            baseURL: 'http://mirari.xyz',
        })
        var ref = null
        new Vue({
            el: '#app',
            data: {
                REINICIAR: 'REINICIAR APLICACIÓN',
                url: '',
                code: '',
            },
            router,
            created:function(){
                self=this
                if ($cookies.get('code')) self.code = $cookies.get('code')
                if ($cookies.get('url')) self.url = $cookies.get('url')
            },
            mounted: function () {
                AndroidFullScreen.immersiveMode()
                if(!self.code || !self.url) self.$router.push('/getCode')
                else self.goIndex()
            },
            methods:{
                goIndex:((get="") => {
                    self.$router.push('/');
                    document.body.style.backgroundColor = "white";
                    if(!self.code || !self.url){
                        self.$router.push('/getCode');
                    }
                    else{
                        if(ref==null){
                            ref = cordova.InAppBrowser.open('http://' + self.url + get, '_blank', 'location=no,toolbar=no')
                            ref.addEventListener('loaderror', function(event){ref.close()});
                            ref.addEventListener("loadstart", (event) => {
                                if (event.url.includes("/SV/GetTicketQR/")){
                                    ref.hide();
                                    self.getQR();
                                }
                            });
                        }else{
                            ref.show();
                        }
                    }
                }),
                getCode:((code) => {
                    ax.post('/api/mirari/mirari/Organization/?api=getCodeOrganization', Qs.stringify({code}))
                    .then((json) => {
                        $cookies.set('code', json.data.organization.code, "3y")
                        $cookies.set('url', json.data.organization.sites.domain, "3y")
                        location.reload()
                    }).catch((error) => {
                        Swal.fire('Ooops!', error.response.data.message, 'error')
                    })
                }),
                getQR:(() => {
                    self.$router.push('/QR');
                    document.body.style.backgroundColor = "transparent";
                    var displayContents = function(err, contents){
                        self.destroyQR(contents)
                    };
                    QRScanner.scan(displayContents);
                    QRScanner.show();
                }),
                destroyQR:((contents=null) => {
                    QRScanner.destroy();
                    self.goIndex();
                    if(contents){
                        script = `self.invoice.ticket = "${contents}"`
                        setTimeout(function() {
                            ref.executeScript({
                                code: script,
                            });
                        }, 300);
                    }
                }),
            },
        });
    },
};
app.initialize();