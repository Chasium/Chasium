<template>
    <div>
        <!-- <canvas
        ref="bgCanvas"
        height="300"
        width="400"
        style="position: absolute; top: 10%; left: 10%; border: 2px solid"
    >
        canvas is not supported.
    </canvas> -->
        <canvas
            ref="MainCanvas"
            height="300"
            width="400"
            style="top: 10%; left: 10%; border: 2px solid"
        >
            canvas is not supported.
        </canvas>
        <img ref="image" />
        <button @click="cleanUp">cleanUp</button>
        <button @click="updateMap">update</button>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useSocketStore } from '@/stores/socket';

export default defineComponent({
    setup() {
        const socketStore = useSocketStore();
        return { socketStore };
    },
    data() {
        return {
            canvas: null,
            ctx: null,
            w: 0,
            h: 0,
            color: '#000000',
            lineWidth: 0,
            isDrawing: false,
            prevX: 0,
            prevY: 0,
            currX: 0,
            currY: 0,
        };
    },
    props: {
        roomID: Number,
    },
    methods: {
        initMap() {
            var canvas = <HTMLCanvasElement>this.$refs['MainCanvas'];
            var ctx = canvas.getContext('2d');
            this.lineWidth = 4;
            this.color = '#FF0000';
            this.ctx = ctx;
            this.w = canvas.width;
            this.h = canvas.height;
            canvas.addEventListener('mousemove', this.drawHandler, false);
            canvas.addEventListener('mousedown', this.drawHandler, false);
            canvas.addEventListener('mouseup', this.drawHandler, false);
            canvas.addEventListener('mouseout', this.drawHandler, false);
            this.canvas = canvas;
        },
        drawHandler(e) {
            if (e.type == 'mousedown') {
                this.socketStore.manager.emitToSocket(
                    'getMapDrawing',
                    this.$props.roomID
                );
                this.updatePos(e);
                this.isDrawing = true;
            } else if (e.type == 'mouseup' || e.type == 'mouseout') {
                this.isDrawing = false;
                this.socketStore.manager.emitToSocket(
                    'updateMapDrawing',
                    this.$props.roomID,
                    this.canvas.toDataURL()
                );
            }
            if (e.type == 'mousemove') {
                if (this.isDrawing) {
                    // console.log('drawing');
                    this.updatePos(e);
                    this.draw();
                }
            }
        },
        updatePos(e) {
            this.prevX = this.currX;
            this.prevY = this.currY;
            this.currX = e.pageX - this.canvas.offsetLeft;
            this.currY = e.pageY - this.canvas.offsetTop;
        },
        draw() {
            // pull from server
            // draw
            // push to server

            this.ctx.beginPath();
            this.ctx.moveTo(this.prevX, this.prevY);
            this.ctx.lineTo(this.currX, this.currY);
            this.ctx.strokeStyle = this.color;
            this.ctx.lineWidth = this.lineWidth;
            this.ctx.stroke();
            this.ctx.closePath();

            // send canvas to server
        },
        cleanUp() {
            this.ctx.clearRect(0, 0, this.w, this.h);
        },
        updateMap() {
            var src = this.canvas.toDataURL();
            this.socketStore.manager.emitToSocket(
                'updateMapDrawing',
                this.$props.roomID,
                src
            );
        },
        updateImage(data) {
            var src = data['Img'];
            if (src != null) {
                this.cleanUp();
                var img = this.$refs['image'];
                img.src = src;
                img.onload = () => {
                    this.ctx.drawImage(img, 0, 0);
                    console.log('loaded');
                };
            }
        },
    },
    created() {
        this.socketStore.manager.subscribe(
            'UpdateMapDrawing',
            this.updateImage
        );
    },
    mounted() {
        this.initMap();
    },
});
</script>
