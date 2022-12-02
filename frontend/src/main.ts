import { createApp } from 'vue';
import { createPinia } from 'pinia';
import axios from 'axios';

import App from './App.vue';
import router from './router';

import '@/assets/css/main.css';
import '@fortawesome/fontawesome-free/css/all.css';

import piniaPersist from 'pinia-plugin-persist';

const app = createApp(App);
const pinia = createPinia();
pinia.use(piniaPersist);

axios.defaults.baseURL = '/api/';

app.use(pinia);
app.use(router);

app.mount('#app');
