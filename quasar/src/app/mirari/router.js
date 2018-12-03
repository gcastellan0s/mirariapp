import auth from '@auth/auth';

import Layout1 from '@/layouts/Layout1'
import Layout1Flex from '@/layouts/Layout1Flex'
import Layout2 from '@/layouts/Layout2'
import Layout2Flex from '@/layouts/Layout2Flex'
import LayoutHorizontalSidenav from '@/layouts/LayoutHorizontalSidenav'
import LayoutWithoutSidenav from '@/layouts/LayoutWithoutSidenav'
import LayoutWithoutNavbar from '@/layouts/LayoutWithoutNavbar'
import LayoutWithoutNavbarFlex from '@/layouts/LayoutWithoutNavbarFlex'
import LayoutBlank from '@/layouts/LayoutBlank'


const routes = [
    //{
        //path: '/',
        //component: () => import('@mirari/dashboard/Dashboard'),
        //beforeEnter: auth.requireAuthenticated,
    //},
    {
        path: '/login/',
        component: () => import ('@/pages/Login'),
        //beforeEnter: auth.requireUnauthenticated,
    },
    {
        path: '/',
        component: Layout2,
        children: [{
        path: '',
            component: () => import('@/components/layouts/Layout2Example')
        }]
    },
    {
        path: '/page-2/',
        component: Layout1,
        children: [{
        path: '',
            component: () => import('@/components/layouts/Layout1Example')
        }]
    },
    {
        path: '/logout/',
        beforeEnter: auth.redirectLogout,
        name:'logout',
    },
]
export default routes