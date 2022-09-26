<template>
    <el-container class="big-frame">
        <el-header class="editor-header">test header</el-header>
        <el-main>test main</el-main>
    </el-container>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
class Data {}
export default defineComponent({
    data() {
        return new Data();
    },
});
</script>

<style lang="scss" scoped>
.big-frame {
    position: fixed;
    width: 100vw;
    height: 100vh;
}

.editor-header {
    background-color: gray;
}
</style>
