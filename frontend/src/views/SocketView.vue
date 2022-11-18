<template>
    <el-container>
        <el-header>SocketIO Test</el-header>
        <div>
            <button @click="fireEventTest">test</button>
            <br />
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
            if (this.user_session == d['User']) {
                this.data = d;
                console.log(d);
            }
        },
        fireEventTest() {
            this.socketStore.manager.emit('init');
        },
    },
    created() {
        this.socketStore.manager.subscribe('init', () => {
            if (!this.userStore.loggedIn) {
                console.log('Not logged!');
            } else {
                let socket_id = this.socketStore.manager.getSocketID();
                this.user_session = this.userStore.session;
                this.socketStore.manager.emitToSocket(
                    'test',
                    socket_id,
                    this.user_session
                );
            }
        });
        this.socketStore.manager.subscribe('response', this.showData);
        this.socketStore.manager.subscribe('connected', () => {
            console.log('server response!');
        });
    },
    data() {
        return {
            data: {},
            user_session: '',
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
        // this.socketStore.manager.removeListener('init');
        // this.socketStore.manager.removeListener('response');
        // this.socketStore.manager.removeListener('connected');
        console.log('unmounted');
    },
});
</script>
