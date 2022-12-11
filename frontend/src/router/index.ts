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
import SocketView from '@/views/SocketView.vue';
import LogoutView from '@/views/LogoutView.vue';
import LobbyView from '@/views/LobbyView.vue';
import RoomView from '@/views/RoomView.vue';
import GameMap from '@/components/GameMap.vue';

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
        {
            path: '/room/:roomID(\\d+)',
            name: 'preparation',
            component: RoomView,
        },
        {
            path: '/lobby',
            name: 'select room',
            component: LobbyView,
        },
        {
            path: '/draw',
            name: 'draw',
            component: GameMap,
        },
    ],
});

export default router;
