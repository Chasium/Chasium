import { createApp } from 'vue';
import { createPinia } from 'pinia';
import axios from 'axios';

import App from './App.vue';
import router from './router';

import '@/assets/css/main.css';

const pinia = createPinia();
const app = createApp(App);

axios.defaults.baseURL = '/api/';

app.use(pinia);
app.use(router);

app.mount('#app');
