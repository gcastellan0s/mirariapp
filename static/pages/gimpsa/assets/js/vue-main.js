var app = {
    initialize:(()=> {
        const router = new VueRouter({routes:[
            { 
                path:'/',
                name: 'index',
            },
            { 
                path:'/QuienesSomos',
                name: 'QuienesSomos',
            },
            { 
                path:'/Plantas',
                name: 'Plantas',
            },
        ]});
        new Vue({
            el: '#app',
            delimiters: ['${', '}'],
            data: {
                name: 'GIMPSA',
            },
            router,
            created:function(){
                self=this
            },
            mounted: function () {
            },
            methods:{
            },
        });
    }),
};
app.initialize()