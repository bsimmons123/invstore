export default class RouterList {
  static routes = {
        root: {
            path: '/',
            name: '/',
            redirect: '/dashboard-default',
        },
        dashboard: {
            path: '/dashboard-default',
            name: 'Dashboard',
            component: 'Dashboard',
        },
        tables: {
            path: '/tables',
            name: 'Tables',
            component: 'Tables',
        },
        billing: {
            path: '/billing',
            name: 'Billing',
            component: 'Billing',
        },
        virtualReality: {
            path: '/virtual-reality',
            name: 'Virtual Reality',
            component: 'VirtualReality',
        },
        rtlPage: {
            path: '/rtl-page',
            name: 'RTL',
            component: 'RTL',
        },
        profile: {
            path: '/profile',
            name: 'Profile',
            component: 'Profile',
        },
        signin: {
            path: '/signin',
            name: 'Signin',
            component: 'Signin',
        },
        signup: {
            path: '/signup',
            name: 'Signup',
            component: 'Signup',
        },
    };
}
