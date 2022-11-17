import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import RegisterView from '../views/RegisterView.vue';
import SocketView from '@/views/SocketView.vue';
import LogoutView from '@/views/LogoutView.vue';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView,
        },
        {
            path: '/register',
            name: 'register',
            component: RegisterView,
        },
        {
            path: '/logout',
            name: 'logout',
            component: LogoutView,
        },
        {
            path: '/chat',
            name: 'chatroom',
            component: SocketView,
        },
    ],
});

export default router;
