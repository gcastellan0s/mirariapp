import api from '../api';

const SET_SELLPOINT = 'SET_SELLPOINT';
const SET_SELLPOINT_FAILURE = 'SET_SELLPOINT_FAILURE';

const getters = {
    sellpoint_data: state => !!state.produts,
};

const Sellpoint = {
    sellpoints: null,
    menus: null,
    products: null,
};

const actions =  {
    set_sellpoint({commit},) {
        return api.set_sellpoint()
        //.then(({res}) => console.log(res))
        .then(({data}) => commit(SET_SELLPOINT, data))
        //.catch((error) => commit(SET_SELLPOINT_FAILURE, error));
    },
};

const mutations = {
    [SET_SELLPOINT](state, data) {
        state.sellpoints = data.Sellpoints
        state.menus = data.Menus
        state.products = data.Products
    },
    [SET_SELLPOINT_FAILURE](state, error) {
        null
    },
};

export default {
    namespaced: true,
    state: Sellpoint,
    getters,
    actions,
    mutations,
};