import Vue from 'vue';
import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faInfoCircle } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import router from './router';
import App from './App.vue';

// to use: <i class="fas fa-coffee"></i> instead of <font-awesome-icon icon="coffee" />
// import { dom } from '@fortawesome/fontawesome-svg-core'
// dom.watch();
// This will kick of the initial replacement of i to svg tags and configure a MutationObserver

library.add(faInfoCircle);
Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.use(BootstrapVue);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
