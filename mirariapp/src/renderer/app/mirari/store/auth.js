import session from '../api/session';
import auth from '../api/auth';

const LOGIN_BEGIN = 'LOGIN_BEGIN';
const LOGIN_FAILURE = 'LOGIN_FAILURE';
const LOGIN_SUCCESS = 'LOGIN_SUCCESS';
const LOGOUT = 'LOGOUT';
const SET_TOKEN = 'SET_TOKEN';
const REMOVE_TOKEN = 'REMOVE_TOKEN';
const TOKEN_STORAGE_KEY = 'TOKEN_STORAGE_KEY';
const SET_USER = 'SET_USER';
const USER = 'USER';
const REMOVE_USER = 'REMOVE_USER';
const SET_USER_FAILURE = 'SET_USER_FAILURE';

const anonymous_user = {
    pk: null,
    visible_username: 'AnonymousUser',
    app: null
}

const initialState = {
    authenticating: false,
    error: false,
    token: null,
    user: anonymous_user,
};

const getters = {
    isAuthenticated: state => !!state.token,
};

const actions =  {
    login({commit}, {username, password}) {
        commit(LOGIN_BEGIN);
        return auth.login(username, password)
        .then(({data}) => commit(SET_TOKEN, data.token))
        .then(() => commit(LOGIN_SUCCESS))
        .catch(() => commit(LOGIN_FAILURE));
    },
    logout({commit}) {
        return auth.logout()
        .then(() => commit(LOGOUT))
        .then(() => commit(REMOVE_USER))
        .finally(() => commit(REMOVE_TOKEN));
    },
    get_user({commit}) {
        return auth.get_user()
        .then((res) => commit(SET_USER, res.data))
        .catch(() => commit(SET_USER_FAILURE));
    },
    initialize({commit}) {
        const token = localStorage.getItem(TOKEN_STORAGE_KEY);
        if (token) {
            commit(SET_TOKEN, token);
        } else {
            commit(REMOVE_TOKEN)
        }
    },
};

const mutations = {
    [LOGIN_BEGIN](state) {
        state.authenticating = true;
        state.error = false;
    },
    [LOGIN_FAILURE](state) {
        state.authenticating = false;
        state.error = true;
    },
    [LOGIN_SUCCESS](state) {
        state.authenticating = false;
        state.error = false;
    },
    [LOGOUT](state) {
        state.authenticating = false;
        state.error = false;
    },
    [SET_TOKEN](state, token) {
        localStorage.setItem(TOKEN_STORAGE_KEY, token);
        session.defaults.headers.Authorization = `JWT ${token}`;
        state.token = token;
    },
    [SET_USER](state, user) {
        localStorage.setItem(USER, user);
        state.user = user;
    },
    [SET_USER_FAILURE](state) {
        localStorage.removeItem(USER);
        state.user = anonymous_user
    },
    [REMOVE_TOKEN](state) {
        localStorage.removeItem(TOKEN_STORAGE_KEY);
        delete session.defaults.headers.Authorization;
        state.token = null;
    },
};

export default {
    namespaced: true,
    state: initialState,
    getters,
    actions,
    mutations,
};