<template>
    <el-container>
        <el-header
            >Room {{ $route.params.roomid }}, created by
            {{ userStore.userName }}</el-header
        >
        <div>
            <button @click="setReady">Ready!</button>
            <br />
            <button @click="startGame">Start!</button>
            <div>
                <button @click="exitRoom">Exit</button>
                <!-- <router-link to="/lobby">Exit</router-link> -->
            </div>
        </div>
    </el-container>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useUserStore } from '@/stores/user';
import { useSocketStore } from '@/stores/socket';
import axios from 'axios';
import type ExitRoomResponse from '@/generated/room/ExitRoomResponse';

export default defineComponent({
    setup() {
        const socketStore = useSocketStore();
        return { socketStore };
    },
    methods: {
        startGame() {
            alert('Game started!');
        },
        setReady() {
            alert('Player ' + this.userStore.userName + ' is ready!');
        },
        async exitRoom() {
            try {
                let response = await axios.post<ExitRoomResponse>(
                    '/room/exit',
                    {
                        roomID: this.$route.params.roomid,
                        userSession: this.userStore.session,
                    }
                );
                if (response.data['code'] == -2) {
                    alert('fail to exit');
                } else if (response.data['code'] == -1) {
                    alert('unknown error');
                } else {
                    this.$router.push('/lobby');
                }
            } catch (err) {
                alert('error');
            }
        },
    },
    data() {
        return {
            data: {},
            // user_session: '',
        };
    },
    computed: {
        userStore() {
            return useUserStore();
        },
    },
    mounted() {
        // console.log('mounted');
        console.log('create room:', this.$route.params.roomid);
    },
    unmounted() {
        console.log('delete room');
        // console.log('unmounted');
    },
});
</script>
