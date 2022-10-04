<template>
    <el-dialog v-model="isCard"></el-dialog>
    <el-dialog v-model="isColumn"></el-dialog>
    <el-dialog v-model="isArea"></el-dialog>
    <el-dialog v-model="isRow"></el-dialog>
    <el-dialog v-model="isProperty"></el-dialog>
</template>

<script lang="ts">
import type { Tree } from '@/trpg/card_template/Tree';
import { defineComponent } from 'vue';

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
});
</script>

<style lang="scss" scoped></style>
