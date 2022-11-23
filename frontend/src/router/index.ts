import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
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
            path: '/main',
            name: 'main',
            redirect: '/main/begin',
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
