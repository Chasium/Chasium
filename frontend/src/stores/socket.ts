import { defineStore } from 'pinia';
import { io } from 'socket.io-client';
import EventEmitter from 'node:events';

export const useSocketStore = defineStore('socket', {
    state() {
        return {
            manager: new SocketManager(),
        };
    },
});

// export declare interface SocketManager {
//     on(event: string, listener: () => void): this;
// }
export class SocketManager extends EventEmitter {
    private socket;
    public eventDict;
    public connected: Boolean;
    constructor() {
        super();
        this.socket = io('http://127.0.0.1:5000/chat', { autoConnect: false });
        this.eventDict = {};
        this.connected = false;
        this.socket.on('fireEvent', this.fireEvent);
    }

    private fireEvent(evName: string, ...args: any[]) {
        this.emit(evName, args);
    }

    public emitToSocket(ev: string, ...args: any[]) {
        this.socket.emit(ev, args);
    }

    public subscribe(ev: string, listener: (args: any[]) => void) {
        this.addListener(ev, listener);
    }

    public unsubscribe(ev: string, listener: (args: any[]) => void) {
        this.removeListener(ev, listener);
    }

    public connect() {
        this.socket.connect();
        this.connected = this.socket.connected;
    }

    public disconnect() {
        this.socket.disconnect();
        this.connected = this.socket.connected;
    }

    public getSocketID(): string {
        if (this.socket.connected) {
            return this.socket.id;
        } else {
            return 'undefined';
        }
    }
}
