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
    methods: {
        showData(d: any) {
            this.data = d;
            console.log(d);
        },
    },
    created() {
        this.socketStore.manager.subscribe('connect', () => {
            if (!this.userStore.loggedIn) {
                console.log('Not logged!');
            } else {
                let socket_id = this.socketStore.manager.getSocketID();
                let user_session = this.userStore.session;
                this.socketStore.manager.emitToSocket(
                    'test',
                    socket_id,
                    user_session
                );
                console.log('socket id: ' + socket_id);
            }
        });
        // this.socketStore.manager.subscribe('response', this.showData);
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
        this.socketStore.manager.connect();
    },
    unmounted() {
        if (this.socketStore.manager.connected) {
            this.socketStore.manager.disconnect();
            console.log('disconnected');
        }
        console.log('unmounted');
    },
});
</script>
