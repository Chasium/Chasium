<template>
    <el-container>
        <el-header>Lobby</el-header>
        <div>
            <p>user {{ userStore.userName }} checking on room list</p>
            <p>
                <button @click="updateRoom">Room available</button>
            </p>
            <p>
                <button @click="createRoom">Be a Host and create room</button>
            </p>
            <room-item
                v-for="(room, index) in rooms"
                v-bind:key="index"
                :roomID="room.roomID"
                @joinRoom="joinRoom(room.roomID)"
            ></room-item>
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

import RoomItem from '@/components/RoomItem.vue';

declare interface Room {
    roomID: Number;
}

export default defineComponent({
    setup() {
        const socketStore = useSocketStore();
        return { socketStore };
    },
    components: {
        RoomItem,
    },
    created() {
        this.socketStore.manager.subscribe('UpdateRoom', this.updateRoom);
    },
    data() {
        return {
            data: {},
            rooms: [] as Room[],
            count: 0,
        };
    },
    methods: {
        async updateRoom() {
            try {
                let response = await axios.post<{ roomID: Number[] }>(
                    '/lobby/getRooms',
                    {}
                );
                var roomList = response.data['roomID'];
                this.rooms = [];
                for (var index in roomList) {
                    this.rooms.push({ roomID: roomList[index] });
                }
            } catch (err) {
                alert('error');
            }
        },
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
                    this.socketStore.manager.emitToSocket('createRoom');
                    this.joinRoom(roomID);
                } else {
                    alert('fail');
                }
            } catch (err) {
                alert('error');
            }
        },
        async joinRoom(roomID: Number) {
            try {
                let response = await axios.post<{ code: Number }>(
                    '/lobby/join',
                    {
                        username: this.userStore.userName,
                        session: this.userStore.session,
                        roomID: roomID,
                    }
                );
                if (response.data['code'] != -1) {
                    this.socketStore.manager.emitToSocket(
                        'joinRoom',
                        roomID,
                        this.userStore.userName
                    );
                    this.socketStore.drawer.emit('joinRoom', roomID);
                    // console.log('join room ' + roomID + '!');
                    this.$router.push('/room/' + roomID);
                } else {
                    alert('something wrong to this room...');
                    this.updateRoom();
                }
            } catch (err) {
                alert('error');
            }
        },
    },
    computed: {
        userStore() {
            return useUserStore();
        },
    },
    mounted() {
        this.updateRoom();
        // console.log(this.socketStore.manager.connected);
    },
    unmounted() {
        // console.log('unmounted');
        this.socketStore.manager.unsubscribe('UpdateRoom', this.updateRoom);
    },
});
</script>
