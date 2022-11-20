<template>
    <el-container>
        <el-header>Lobby</el-header>
        <div>
            <p>Room of {{ userStore.userName }}</p>
            <p>
                <button @click="createRoom">Be a Host and create room</button>
            </p>
            <p>
                <button>Be a player and join room</button>
            </p>
            <br />
            <div>
                <router-link to="/logout">logout</router-link>
            </div>
        </div>
    </el-container>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useUserStore } from '@/stores/user';
import { useSocketStore } from '@/stores/socket';
import axios from 'axios';
import type RoomCreationResponse from '@/generated/lobby/RoomCreationResponse';

export default defineComponent({
    setup() {
        const socketStore = useSocketStore();
        return { socketStore };
    },
    methods: {
        async createRoom() {
            try {
                let response = await axios.post<RoomCreationResponse>(
                    '/lobby/create',
                    {
                        hostName: this.userStore.userName,
                        hostSession: this.userStore.session,
                    }
                );
                let roomID = response.data['id'];
                if (roomID != -1) {
                    this.$router.push('/room/' + roomID);
                } else {
                    alert('fail');
                }
            } catch (err) {
                alert('error');
            }
        },
        async joinRoom() {},
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
        // console.log('mounted');
    },
    unmounted() {
        // console.log('unmounted');
    },
});
</script>
