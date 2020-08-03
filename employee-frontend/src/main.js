import Vue from 'vue'
import Buefy from 'buefy'
import { ValidationProvider, ValidationObserver } from 'vee-validate'
import App from './App.vue'

import 'buefy/dist/buefy.css'
import './validation/validator.js'

Vue.config.productionTip = false
Vue.use(Buefy)
Vue.component('ValidationProvider', ValidationProvider)
Vue.component('ValidationObserver', ValidationObserver)

new Vue({
  render: h => h(App),
}).$mount('#app')
