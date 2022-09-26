<template>
    <el-container class="big-frame">
        <el-header class="editor-header" height="2em">test header</el-header>
        <el-main class="editor-frame">
            <el-container class="editor-container">
                <el-aside width="20em" class="editor-aside"
                    ><TemplateEditorAside
                /></el-aside>
                <el-main class="editor-main"></el-main>
            </el-container>
        </el-main>
    </el-container>
</template>

<script lang="ts">
import { useTEStore } from '@/stores/templateEditor';
import { defineComponent } from 'vue';
import TemplateEditorAside from '../components/template_editor/TemplateEditorAside.vue';

class Data {}

export default defineComponent({
    data() {
        return new Data();
    },
    computed: {
        teStore() {
            return useTEStore();
        },
    },
    components: { TemplateEditorAside },
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

.editor-frame {
    padding: 0px;
}

.editor-container {
    width: 100%;
    height: 100%;
}

.editor-main {
    padding: 0px;
}
</style>
