import rules from '@/app/mirari/api/rules';

const routes = [
    {
        path: '/',
        component: () => import ('./views/components/Layout'),
        children: [{
            path: '/',
            component: () => import ('./views/Sellpoint'),
            name: 'SV',
            beforeEnter: rules.requireAuthenticated
        }],
    },
]
export default routes