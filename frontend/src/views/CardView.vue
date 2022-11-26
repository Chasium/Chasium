<template>
    <el-button @click="showDialog">show Dialog</el-button>
    <div id="dialog-cover" style="display: none"></div>
    <dialog id="dialog-box">
        <card-script-dialog />
        <div style="margin-top: 50px; margin-left: 50%">
            <el-button @click="noDialog">取 消</el-button>
            <el-button type="primary" @click="noDialog">导 入</el-button>
        </div>
    </dialog>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CardScriptDialog from '../components/CardScriptDialog.vue';
export default defineComponent({
    data() {
        return {};
    },
    components: { CardScriptDialog },
    methods: {
        showDialog() {
            //把后面的全都遮盖住
            document.getElementById('dialog-cover').style.display = 'block';
            document.getElementById('dialog-box').style.display = 'block';
            console.log('show');
        },
        noDialog() {
            document.getElementById('dialog-cover').style.display = 'none';
            document.getElementById('dialog-box').style.display = 'none';
            console.log('show');
        },
    },
});
</script>

<style>
#dialog-cover {
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
    width: 100%;
    background-color: #000;
    opacity: 0.3;
    filter: alpha(opacity=30);
}
#dialog-box {
    width: 500px;
    height: 800px;
    border: none !important;
    border-radius: calc(5px * var(--ratio));
    box-shadow: 0 0 #0000, 0 0 #0000, 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    padding: 1.6rem;
    max-width: 400px;
}
</style>
