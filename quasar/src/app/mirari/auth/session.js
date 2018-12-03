import axios from 'axios'
import M from '@mirari/variables/M'

const session = axios.create({
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken',
  baseURL: M.API,
})

export default session
