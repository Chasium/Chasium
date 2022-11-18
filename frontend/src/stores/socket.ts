import { defineStore } from 'pinia';
import { io } from 'socket.io-client';
import EventEmitter from 'eventemitter3';

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
    public connected: Boolean = false;
    constructor() {
        super();
        this.socket = io('http://127.0.0.1:5000/chat', { autoConnect: false });
        this.eventDict = {};
        this.socket.on('FireEvent', (args: any) => {
            const ev = args['EventName'];
            const data = args['Data'];
            console.log(args);
            console.log('Event', ev, 'Fire!');
            console.log('args:', data);
            this.emit(ev, data);
        });
        this.socket.on('connect', () => {
            console.log(this.socket.connected);
        });
    }

    public emitToSocket(ev: string, ...args: any[] | []) {
        console.log('Event emitted:', ev);
        console.log('args:', ...args);
        if (args.length == 0) {
            this.socket.emit(ev);
        } else {
            this.socket.emit(ev, ...args);
        }
    }

    public subscribe(ev: string, listener: (args: any[]) => void) {
        console.log('Event subscribed:', ev);
        this.addListener(ev, listener);
    }

    public unsubscribe(ev: string, listener: (args: any[]) => void) {
        console.log('Event', ev, 'unsubscribed');
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
