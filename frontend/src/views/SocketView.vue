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
                <button @click="logout">Logout</button>
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
        async fireEventTest() {
            this.socketStore.manager.emit('init');
        },
        async logout() {
            if (this.socketStore.manager.connected) {
                this.socketStore.manager.emitToSocket(
                    'leave',
                    this.userStore.session
                );
                this.socketStore.manager.disconnect();
                console.log('disconnected');
                this.$router.push('/logout');
            } else {
                console.log('fucked');
            }
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
        this.socketStore.manager.subscribe('disconnected', () => {
            console.log('disconnected!');
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
        this.socketStore.manager.emitToSocket('join', this.userStore.session);
    },
    unmounted() {
        console.log('unmounted');
    },
});
</script>
