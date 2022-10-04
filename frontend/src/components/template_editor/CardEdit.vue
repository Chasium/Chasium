<template>
    <el-form>
        <el-form-item label="模板名称">
            <el-input v-model="name"></el-input>
        </el-form-item>
        <el-form-item label="模板描述">
            <el-input v-model="description"></el-input>
        </el-form-item>
        <el-form-item label="是否需要检验">
            <el-switch v-model="needCheck"></el-switch>
        </el-form-item>
        <el-form-item label="检验脚本"> </el-form-item>
    </el-form>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

class Data {
    name = '';
    description = '';
    needCheck = false;
    checkScript = '';
    coverPropertyId = -1;
    cardDescriptionScript = '';
    inGameCardScript = '';
}

export default defineComponent({
    data() {
        return new Data();
    },
});
</script>

<style lang="scss" scoped></style>
