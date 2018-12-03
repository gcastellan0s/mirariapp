const routes = [
    {
        path: '/crye/',
        component: () => import ('@/layout/LayoutWithoutSidenav'),
        children: [
            {
                path: '/crye/cotizador/',
                component: () => simport ('./views/Cotizador'),
                name: 'crye__cotizador',
                //beforeEnter: rules.requireAuthenticated
            },
            {
                path: '/crye/cotizador-financiero/',
                component: () => import ('./views/Cotizador_financiero'),
                name: 'crye__cotizador_financiero',
                //beforeEnter: rules.requireAuthenticated
            },
        ],
    },
]
export default routes