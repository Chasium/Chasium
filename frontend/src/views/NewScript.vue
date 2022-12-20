<template>
    <h1>剧本编辑器</h1>
    <md-editor
        toolbarsExclude="['mermaid', 'image', 'github']"
        v-model="text"
    />
    <el-button @click="onclick" id="button">提交剧本</el-button>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MdEditor from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';

export default defineComponent({
    components: { MdEditor },
    data() {
        return { text: '' };
    },
    methods: {
        onclick() {
            // TODO 将剧本中的内容和脚本分别存入后端
            console.log(this.text);
            alert('提交成功');
        },
    },
});
</script>

<style>
h1 {
    margin-left: 5px;
}
#button {
    margin-top: 20px;
    float: right;
}
</style>
