import store from '@/store';

const requireAuthenticated = (to, from, next) => {
    store.dispatch('auth/initialize')
    .then(() => {
        if (!store.getters['auth/isAuthenticated']) {
            next('/login/');
        } else {
            next();
        }
    });
};

const requireUnauthenticated = (to, from, next) => {
    store.dispatch('auth/initialize')
    .then(() => {
        if (store.getters['auth/isAuthenticated']) {
            next('');
        } else {
            next();
        }
    });
};

const redirectLogout = (to, from, next) => {
    store.dispatch('auth/logout')
    .then(() => next('/login/'));
};

export default {
    requireAuthenticated,
    requireUnauthenticated,
    redirectLogout
};