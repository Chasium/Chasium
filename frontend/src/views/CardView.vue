<template>
    <el-button @click="showDialog">show Dialog</el-button>
    <div id="dialog-cover" style="display: none"></div>
    <dialog id="dialog-box" style="display: none">
        <card-script-dialog ref="cardscriptdialog" id="scriptDialog" />
        <div style="margin-top: 50px; margin-left: 70%">
            <el-button @click="noDialog">取 消</el-button>
            <el-button type="primary" @click="importScript">导 入</el-button>
        </div>
    </dialog>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CardScriptDialog from '../components/CardScriptDialog.vue';
import axios from 'axios';
import type AddCardScriptResponse from '@/generated/script/AddCardScriptResponse';

export default defineComponent({
    data() {
        return {
            uploadSuccess: false,
        };
    },
    components: { CardScriptDialog },
    created() {
        this.uploadSuccess = false;
    },
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
            console.log('hidden');
        },
        async importScript() {
            const val = this.$refs.cardscriptdialog.updateModelValue();
            console.log('get val:\n', val);
            // TODO: 把脚本存入数据库
            try {
                let response = await axios.post<AddCardScriptResponse>(
                    '/script/add',
                    {
                        scriptContent: val,
                    }
                );
                this.uploadSuccess = false;
                if (response.data['code'] === 0) {
                    alert('提交成功');
                    this.uploadSuccess = true;
                    this.$router.push('/login');
                    document.getElementById('dialog-cover').style.display =
                        'none';
                    document.getElementById('dialog-box').style.display =
                        'none';
                } else if (response.data['code'] !== 0) {
                    alert('不合法');
                } else {
                    alert('未知错误');
                }
            } catch (err) {
                alert('异常');
            }
            this.$router.push('/card');
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
    border: none !important;
    border-radius: calc(5px * var(--ratio));
    box-shadow: 0 0 #0000, 0 0 #0000, 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    padding: 1.6rem;
    max-width: 600px;
}
</style>
