import axios from 'axios';

const session = axios.create({
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFToken',
    baseURL: '//'+require('@/../../package.json').api,
});

export default session;