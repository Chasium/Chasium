<template>
    <el-dialog v-model="isCard">
        <CardEdit />
    </el-dialog>
    <el-dialog v-model="isColumn"></el-dialog>
    <el-dialog v-model="isArea"></el-dialog>
    <el-dialog v-model="isRow"></el-dialog>
    <el-dialog v-model="isProperty"></el-dialog>
</template>

<script lang="ts">
import type { Tree } from '@/trpg/card_template/Tree';
import { defineComponent } from 'vue';
import CardEdit from './CardEdit.vue';

class Data {
    isCard = false;
    isColumn = false;
    isArea = false;
    isRow = false;
    isProperty = false;
    currentNode?: Tree = undefined;
}

export default defineComponent({
    data() {
        return new Data();
    },
    components: { CardEdit },
});
</script>

<style lang="scss" scoped></style>
