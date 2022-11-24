<template>
    <el-container>
        <el-header
            >Room {{ $route.params.roomID }}, created by
            {{ userStore.userName }}</el-header
        >
        <p>You are in this room as a {{ userCharater }}.</p>
        <div>
            <button @click="setReady">Ready!</button>
            <br />
            <button @click="getPlayerNames">getPlayers</button>
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
    created() {
        this.socketStore.manager.subscribe('DismissRoom', () => {
            this.forceExit();
        });
        this.socketStore.manager.subscribe('NewMsg', (data: any) => {
            console.log(data['Msg']);
        });
    },
    methods: {
        forceExit() {
            let roomID = Number(this.$route.params.roomID);
            this.socketStore.manager.emitToSocket(
                'leaveRoom',
                roomID,
                this.userStore.userName
            );
            this.$router.push('/lobby');
        },
        startGame() {
            alert('Game started!');
        },
        setReady() {
            alert('Player ' + this.userStore.userName + ' is ready!');
        },
        async checkInRoom() {
            try {
                let response = await axios.post<{ code: Number; host: string }>(
                    '/room/check',
                    {
                        roomID: this.$route.params.roomID,
                        userSession: this.userStore.session,
                    }
                );
                if (response.data['code'] == 1) {
                    this.userCharater = 'Host';
                    this.hostName = response.data['host'];
                } else if (response.data['code'] == 2) {
                    this.userCharater = 'Player';
                } else if (response.data['code'] == -2) {
                    alert('you are not allowed into this room!');
                    this.$router.push('/lobby');
                } else {
                    alert('invalid room number');
                    this.$router.push('/lobby');
                }
            } catch (err) {
                alert('error');
            }
        },
        async getPlayerNames() {
            let response = await axios.post<{ players: string[] }>(
                '/room/players',
                {
                    roomID: this.$route.params.roomID,
                    userSession: this.userStore.session,
                }
            );
            console.log(response.data['players']);
        },

        async exitRoom() {
            try {
                let response = await axios.post<ExitRoomResponse>(
                    '/room/exit',
                    {
                        roomID: this.$route.params.roomID,
                        userSession: this.userStore.session,
                    }
                );
                if (response.data['code'] == -2) {
                    alert('fail to exit');
                } else if (response.data['code'] == -1) {
                    alert('unknown error');
                } else if (response.data['code'] == 2) {
                    let roomID = Number(this.$route.params.roomID);
                    this.socketStore.manager.emitToSocket(
                        'dismissRoom',
                        roomID,
                        this.userStore.userName
                    );
                } else {
                    this.forceExit();
                }
            } catch (err) {
                alert('error');
            }
        },
    },
    data() {
        return {
            data: {},
            userCharater: 'unknown',
            hostName: '',
            playerNames: [],
        };
    },
    computed: {
        userStore() {
            return useUserStore();
        },
    },
    mounted() {
        // console.log('mounted');
        this.checkInRoom();
        // console.log('create room:', this.$route.params.roomID);
    },
    unmounted() {
        // console.log('unmounted');
        // this.socketStore.manager.unsubscribe('DismissRoom', () => {
        //     alert('Host has left!');
        //     this.forceExit();
        // });
        // this.socketStore.manager.unsubscribe('NewMsg', (data: any) => {
        //     console.log(data['Msg']);
        // });
    },
});
</script>
