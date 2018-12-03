// import something here
import globals from '@mirari/variables/globals'

// leave the export, even if you don't use it
export default ({ app, router, Vue }) => {
  // something to do
  // Global RTL flag
  Vue.mixin({
    data: globals
  })
}
