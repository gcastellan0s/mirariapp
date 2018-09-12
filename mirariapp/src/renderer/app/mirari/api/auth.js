import session from './session';
var qs = require('qs');
export default {
    login(username, password) {
        return session.post('/api-token-auth/', qs.stringify({username, password}));
    },
    logout() {
        return session.post('/rest-auth/logout/');
    },
    get_user() {
        return session.post('/api/GetUserApiView/mirari/get/User/');
    },
};
