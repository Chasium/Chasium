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
    // background-color: #363d40;
    // // 给头部设置一下弹性布局
    // display: flex;
    // // 让它贴标左右对齐
    // justify-content: space-between;
    // // 清空图片左侧padding
    padding-left: 0;
    padding-right: 0;
    // // 按钮居中
    // align-items: center;
    // // 文本颜色
    // color: #fff;
    // // 设置文本字体大小
    // font-size: 20px;
    // // 嵌套
    // > div {
    //     // 弹性布局
    //     display: flex;
    //     // 纵向上居中对齐
    //     align-items: center;
    //     // 给文本和图片添加间距，使用类选择器
    //     span {
    //         margin-left: 15px;
    //     }
    // }
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
