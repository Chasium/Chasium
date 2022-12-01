<template>
    <div style="width: 550px">
        <h3>插入模型</h3>
        <CardScriptEditor style="width: 550px" ref="editor" />
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CardScriptEditor from './CardScriptEditor.vue';

export default defineComponent({
    components: { CardScriptEditor },
    methods: {
        updateModelValue() {
            const val = this.$refs.editor.childMethod();
            // console.log('get from Editor:', val);
            return val;
        },
    },
});
</script>
