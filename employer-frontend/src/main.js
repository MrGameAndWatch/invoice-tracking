import Vue from 'vue'
import Buefy from 'buefy'
import App from './App.vue'

import 'buefy/dist/buef.css'

Vue.config.productionTip = false
Vue.use(Buefy)

new Vue({
  render: h => h(App),
}).$mount('#app')
