// import something here
import Popper from 'popper.js'

// leave the export, even if you don't use it
export default ({ app, router, Vue }) => {
  // something to do
  Popper.Defaults.modifiers.computeStyle.gpuAcceleration = false
}
