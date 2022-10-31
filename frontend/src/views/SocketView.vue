<template>
    <el-container>
        <el-header>SocketIO Test</el-header>
        <div>
            <span>Flask response</span>
            <br />
            <span>{{ data }}</span>
            <div>
                <router-link to="/logout">Logout</router-link>
            </div>
        </div>
    </el-container>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useUserStore } from '@/stores/user';
import { useSocketStore } from '@/stores/socket';
import axios from 'axios';

export default defineComponent({
    setup() {
        const socketStore = useSocketStore();
        return { socketStore };
    },
    created() {
        this.socketStore.socket.on('connect', () => {
            if (!this.userStore.loggedIn) {
                console.log('Not logged!');
            } else {
                let socket_id = this.socketStore.socket.id;
                let user_session = this.userStore.session;
                this.socketStore.socket.emit('test', socket_id, user_session);
                console.log('socket id: ' + socket_id);
            }
        });
        this.socketStore.socket.on('response', (data) => {
            this.data = data;
            console.log(data);
        });
    },
    data() {
        return {
            data: {},
        };
    },
    computed: {
        userStore() {
            return useUserStore();
        },
    },
    mounted() {
        console.log('mounted');
        this.socketStore.socket.connect();
    },
    unmounted() {
        if (this.socketStore.socket.connected) {
            this.socketStore.socket.disconnect();
            console.log('disconnected');
        }
        console.log('unmounted');
    },
});
</script>
