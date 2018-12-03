// import something here
import M from '@mirari/variables/M'

// leave the export, even if you don't use it
export default ({ app, router, Vue }) => {
  // something to do
  Vue.mixin({
    data: M
  })
}
