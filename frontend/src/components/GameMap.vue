<template>
    <div>
        <canvas
            ref="bgCanvas"
            height="300"
            width="400"
            style="position: absolute; top: 30%; left: 30%; border: 2px solid"
        ></canvas>
        <canvas
            ref="otherCanvas"
            height="300"
            width="400"
            style="position: absolute; top: 30%; left: 30%; border: 2px solid"
        ></canvas>
        <canvas
            ref="mainCanvas"
            height="300"
            width="400"
            style="position: absolute; top: 30%; left: 30%; border: 2px solid"
        ></canvas>
        <button v-show="isHost" @click="cleanUp">cleanUp</button><br />
        <input v-show="isHost" type="file" id="imageLoader" />
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useSocketStore } from '@/stores/socket';
import { bg } from 'element-plus/es/locale';

export default defineComponent({
    setup() {
        const socketStore = useSocketStore();
        return { socketStore };
    },
    data() {
        return {
            mainCanvas: null,
            bgCanvas: null,
            otherCanvas: null,
            otherCtx: null,
            mainCtx: null,
            bgCtx: null,
            w: 0,
            h: 0,
            lineWidth: 0,
            isDrawing: false,
        };
    },
    props: {
        roomID: Number,
        color: String,
        isHost: Boolean,
    },
    methods: {
        initGameMap() {
            var bgCanvas = <HTMLCanvasElement>this.$refs['bgCanvas'];
            var bgCtx = bgCanvas.getContext('2d');
            this.bgCanvas = bgCanvas;
            this.bgCtx = bgCtx;

            var otherCanvas = <HTMLCanvasElement>this.$refs['otherCanvas'];
            var otherCtx = otherCanvas.getContext('2d');
            this.otherCanvas = otherCanvas;
            this.otherCtx = otherCtx;

            var canvas = <HTMLCanvasElement>this.$refs['mainCanvas'];
            var ctx = canvas.getContext('2d');
            this.mainCanvas = canvas;
            this.mainCtx = ctx;

            this.lineWidth = 4;
            this.w = canvas.width;
            this.h = canvas.height;

            canvas.addEventListener('mousemove', this.drawHandler, false);
            canvas.addEventListener('mousedown', this.drawHandler, false);
            canvas.addEventListener('mouseup', this.drawHandler, false);
            canvas.addEventListener('mouseout', this.drawHandler, false);

            var imageLoader = document.getElementById('imageLoader');
            imageLoader.addEventListener('change', this.updateBg, false);
        },
        drawHandler(e) {
            var x = e.pageX - this.mainCanvas.offsetLeft;
            var y = e.pageY - this.mainCanvas.offsetTop;
            this.draw(this.mainCtx, x, y, this.$props.color, e.type);
            if (e.type != 'mousemove' || this.isDrawing) {
                this.socketStore.drawer.emit(
                    'playerDrawing',
                    this.$props.roomID,
                    x,
                    y,
                    this.$props.color,
                    e.type
                );
            }
        },
        draw(ctx, currX, currY, color, type) {
            if (type == 'mousedown') {
                // console.log('draw');
                this.isDrawing = true;
                ctx.beginPath();
                ctx.moveTo(currX, currY);
            } else if (type == 'mouseup' || type == 'mouseout') {
                this.isDrawing = false;
                ctx.closePath();
            } else if (type == 'mousemove') {
                if (this.isDrawing) {
                    ctx.strokeStyle = color;
                    ctx.lineWidth = this.lineWidth;
                    ctx.lineTo(currX, currY);
                    ctx.stroke();
                }
            }
        },
        drawOther(data) {
            var x = data['x'];
            var y = data['y'];
            var color = data['color'];
            var type = data['type'];
            if (type == 'mousedown') {
                this.otherCtx.beginPath();
                this.otherCtx.moveTo(x, y);
            } else if (type == 'mouseup' || type == 'mouseout') {
                this.otherCtx.closePath();
            } else if (type == 'mousemove') {
                this.otherCtx.strokeStyle = color;
                this.otherCtx.lineWidth = this.lineWidth;
                this.otherCtx.lineTo(x, y);
                this.otherCtx.stroke();
            }
        },
        cleanUp() {
            this.socketStore.drawer.emit('cleanMapDrawing', this.$props.roomID);
        },
        CleanUp() {
            this.mainCtx.clearRect(0, 0, this.w, this.h);
            this.otherCtx.clearRect(0, 0, this.w, this.h);
        },
        updateBg(e) {
            var reader = new FileReader();
            var ctx = this.bgCtx;
            var canvas = this.bgCanvas;
            var roomID = this.$props.roomID;
            var drawer = this.socketStore.drawer;
            reader.onload = function (event) {
                var img = new Image();
                img.onload = function () {
                    ctx.drawImage(img, 0, 0);
                    var src = canvas.toDataURL('image/jpeg', 0.6);
                    drawer.emit('updateBg', roomID, src);
                };
                img.src = event.target?.result;
            };
            reader.readAsDataURL(e.target?.files[0]);
        },
        UpdateBg(data) {
            var ctx = this.bgCtx;
            var img = new Image();
            img.onload = function () {
                ctx.drawImage(img, 0, 0);
            };
            img.src = data['src'];
        },
    },
    created() {
        this.socketStore.drawer.on('UpdateMapDrawing', this.drawOther);
        this.socketStore.drawer.on('CleanMapDrawing', this.CleanUp);
        this.socketStore.drawer.on('UpdateBg', this.UpdateBg);
    },
    mounted() {
        this.socketStore.drawer.connect();
        this.initGameMap();
    },
    unmounted() {
        this.socketStore.drawer.off('UpdateMapDrawing', this.drawOther);
        this.socketStore.drawer.off('CleanMapDrawing', this.CleanUp);
        this.socketStore.drawer.off('UpdateBg', this.UpdateBg);
    },
});
</script>
