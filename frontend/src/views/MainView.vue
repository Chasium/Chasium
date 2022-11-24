<template>
    <div class="common-layout">
        <el-container class="main_container">
            <el-header>
                <common-header />
            </el-header>
            <el-container>
                <el-aside width="200px">
                    <common-aside />
                </el-aside>
                <el-main>
                    <RouterView />
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script lang="ts">
import CommonAside from '@/components/CommonAside.vue';
import CommonHeader from '@/components/CommonHeader.vue';
import { defineComponent } from 'vue';
export default defineComponent({
    data() {
        return {};
    },
    components: {
        CommonAside,
        CommonHeader,
    },
});
</script>

<style lang="scss" scoped>
.common-layout {
    --el-header-height: 60px;
}
.home_container {
    height: 100%;
}
.el-header {
    padding-left: 0;
    padding-right: 0;
}
.el-aside {
    background-color: #313743;
    height: calc(100vh - var(--el-header-height));
    overflow: hidden;
    .el-menu {
        border-right: none;
    }
}
.el-main {
    background-color: #e9edf1;
    height: calc(100vh - var(--el-header-height));
}
.iconfont {
    margin-right: 10px;
}
</style>
