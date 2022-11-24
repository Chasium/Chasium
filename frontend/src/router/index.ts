import { createRouter, createWebHistory } from 'vue-router';
import LoginView from '../views/LoginView.vue';
import RegisterView from '../views/RegisterView.vue';
import MainView from '@/views/MainView.vue';
import UserView from '@/views/UserView.vue';
import BeginView from '@/views/BeginView.vue';
import MyScriptView from '@/views/MyScriptView.vue';
import ScriptView from '@/views/ScriptView.vue';
import TemplateCardView from '@/views/TemplateCardView.vue';
import MyTemplateCardView from '@/views/MyTemplateCardView.vue';
import CardView from '@/views/CardView.vue';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/login',
            name: 'login',
            component: LoginView,
        },
        {
            path: '/register',
            name: 'register',
            component: RegisterView,
        },
        {
            path: '/',
            name: 'main',
            redirect: '/login',
            component: MainView,
            children: [
                { path: 'user', component: UserView },
                { path: 'begin', component: BeginView },
                { path: 'card', component: CardView },
                { path: 'script', component: ScriptView },
                { path: 'myscript', component: MyScriptView },
                { path: 'template', component: TemplateCardView },
                { path: 'mytemplate', component: MyTemplateCardView },
            ],
        },
    ],
});

export default router;
