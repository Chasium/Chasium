import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import TemplateEditView from '../views/TemplateEditView.vue';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView,
        },
        {
            path: '/template-edit',
            name: 'template-edit',
            component: TemplateEditView,
        },
        {
            path: '/register',
            name: 'register',
            component: RegisterView,
        },
    ],
});

export default router;
