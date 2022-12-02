<template>
    <el-menu
        active-text-color="#ffd04b"
        background-color="#545c64"
        class="el-menu-vertical-demo"
        default-active="user"
        text-color="#fff"
        @open="handleOpen"
        @close="handleClose"
    >
        <el-menu-item @click="clickBegin" index="begin">
            <el-icon><VideoPlay /></el-icon>
            <span>游戏大厅</span>
        </el-menu-item>
        <el-menu-item @click="clickCard" index="card">
            <el-icon><Postcard /></el-icon>
            <span>人物卡</span>
        </el-menu-item>
        <el-sub-menu index="1">
            <template #title>
                <el-icon><Memo /></el-icon>
                <span>人物卡模板</span>
            </template>
            <el-menu-item-group>
                <el-menu-item @click="clickMyTemplate" index="1-1"
                    >我的模板</el-menu-item
                >
                <el-menu-item @click="clickTemplate" index="1-2"
                    >可用模板</el-menu-item
                >
            </el-menu-item-group>
        </el-sub-menu>
        <el-sub-menu index="2">
            <template #title>
                <el-icon><Collection /></el-icon>
                <span>剧本</span>
            </template>
            <el-menu-item-group>
                <el-menu-item @click="clickMyScript" index="2-1"
                    >我的剧本</el-menu-item
                >
                <el-menu-item @click="clickScript" index="2-2"
                    >可用剧本</el-menu-item
                >
            </el-menu-item-group>
        </el-sub-menu>
    </el-menu>
</template>

<script lang="ts">
import {
    User,
    VideoPlay,
    Postcard,
    Collection,
    Setting,
    Memo,
} from '@element-plus/icons-vue';
import { defineComponent } from 'vue';

export default defineComponent({
    data() {
        return {};
    },
    methods: {
        handleOpen(key: string, keyPath: string[]) {
            console.log(key, keyPath);
        },
        handleClose(key: string, keyPath: string[]) {
            console.log(key, keyPath);
        },
        clickBegin() {
            if (this.$route.path != '/begin') {
                this.$router.push('/begin');
            }
        },
        clickCard() {
            if (this.$route.path != '//card') {
                this.$router.push('/card');
            }
        },
        clickTemplate() {
            if (this.$route.path != '/template') {
                this.$router.push('/template');
            }
        },
        clickMyTemplate() {
            if (this.$route.path != '/mytemplate') {
                this.$router.push('/mytemplate');
            }
        },
        clickScript() {
            if (this.$route.path != '/script') {
                this.$router.push('/script');
            }
        },
        clickMyScript() {
            if (this.$route.path != '/myscript') {
                this.$router.push('myscript');
            }
        },
    },
    components: {
        VideoPlay,
        Postcard,
        Collection,
        Memo,
    },
    computed: {},
});
</script>

<style lang="scss">
.el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 100vh;
}
span {
    font-size: 15px;
}
</style>
