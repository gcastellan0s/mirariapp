import Vue from 'vue';
import Vuex from 'vuex';
import createLogger from 'vuex/dist/logger';

// mirari
import auth from '@/app/mirari/store/auth';
import SV from '@/app/SV/store/sellpoint';

const debug = process.env.NODE_ENV !== 'production';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    // mirari
    auth,
    SV,
  },
  strict: debug,
  plugins: debug ? [createLogger()] : [],
});