<template>
    <div style="width: 550px">
        <el-form :model="form" :ref="formRef" :rules="rules">
            <el-form-item label="脚本功能" prop="name">
                <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="脚本描述" prop="description">
                <el-input
                    type="textarea"
                    v-model="form.description"
                    placeholder="请输入脚本描述"
                    style="height: 120px"
                    :rows="5"
                ></el-input>
            </el-form-item>
            <el-form-item>
                <CardScriptEditor id="editor" ref="editor" />
            </el-form-item>
        </el-form>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CardScriptEditor from './CardScriptEditor.vue';

export default defineComponent({
    components: { CardScriptEditor },
    data() {
        return {
            codeContent: '',
            formRef: 'cardScriptEditor',
            form: {
                name: '',
                description: '',
            },
            rules: {
                name: [
                    {
                        required: true,
                        message: '请输入脚本功能',
                        trigger: 'blur',
                    },
                    {
                        min: 1,
                        max: 20,
                        message: '长度在 1 到 20 个字符',
                        trigger: 'blur',
                    },
                ],
                description: [
                    {
                        required: true,
                        message: '请输入脚本代码',
                        trigger: 'blur',
                    },
                    {
                        min: 1,
                        max: 200,
                        message: '长度在 1 到 200 个字符',
                        trigger: 'blur',
                    },
                ],
            },
        };
    },
    methods: {
        updateModelValue() {
            const val = this.$refs.editor.childMethod();
            // console.log('get from Editor:', val);
            return val;
        },
    },
});
</script>

<style>
#editor {
    width: 550px;
}
</style>
