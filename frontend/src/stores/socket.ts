import { defineStore } from 'pinia';
import { io } from 'socket.io-client';

export const useSocketStore = defineStore('socket', {
    state() {
        return {
            socket: io('http://127.0.0.1:5000/chat', { autoConnect: false }),
        };
    },
});
