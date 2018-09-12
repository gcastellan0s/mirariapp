import rules from '@/app/mirari/api/rules';

const routes = [
    {
        path: '/login/',
        component: () => import ('@/app/mirari/views/Login'),
        beforeEnter: rules.requireUnauthenticated,
    },
    {
        path: '/logout/',
        beforeEnter: rules.redirectLogout,
        name:'logout',
    },
]
export default routes