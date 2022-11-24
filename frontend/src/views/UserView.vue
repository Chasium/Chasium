<template>
    <el-row>
        <el-col :span="8">
            <el-card class="box-user">
                <div class="user">
                    <img src="@/assets/images/user.png" />
                    <div class="user-info">
                        <p class="name">憨憨小胖</p>
                        <p class="id">
                            用户名：<span>{{ id }}</span>
                        </p>
                        <p class="time">游戏总时长：<span>100小时</span></p>
                    </div>
                </div>
                <div class="login-info">
                    <p>
                        上次登录时间：<span>{{ time }}</span>
                    </p>
                </div>
            </el-card>
            <el-card class="box-data"> </el-card>
        </el-col>
        <el-col :span="16">
            <el-card class="box-game-data">
                <el-scrollbar max-height="780px">
                    <div
                        v-for="item in gameRecord"
                        :key="item.id"
                        class="scrollbar-demo-item"
                    >
                        <img :src="item.img" />
                        <p>{{ item.name }}</p>
                        <p>{{ item.beginTime }} ~ {{ item.endTime }}</p>
                    </div>
                </el-scrollbar>
            </el-card>
        </el-col>
    </el-row>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useUserStore } from '@/stores/user';
export default defineComponent({
    data() {
        return {
            id: 'Boinzz',
            time: '2022/11/23 18:55:00',
            gameRecord: [
                {
                    img: '@/assets/images/Cthulhu.png',
                    name: '龙族世界',
                    id: 1,
                    beginTime: '2022年10月4日20:00',
                    endTime: '2022年10月4日23:00',
                },
                {
                    img: '@/assets/images/Cthulhu.png',
                    name: '克苏鲁的呼唤',
                    id: 2,
                    beginTime: '2022年10月4日20:00',
                    endTime: '2022年10月4日23:00',
                },
            ],
        };
    },
    methods: {
        async getId() {
            return 'Boinzz';
        },
        async getTime() {
            return '2022/11/23 18:55:00';
        },
    },
});
</script>

<style lang="scss" scoped>
.box-user {
    min-width: 450px;
    min-height: 280px;
}
.user {
    padding-bottom: 20px;
    margin-bottom: 20px;
    border-bottom: 1.5px solid #ccc;
    display: flex;
    align-items: center;
    img {
        height: 180px;
        width: 180px;
        border-radius: 50%;
    }
    .user-info {
        margin-left: 30px;
        .name {
            font-size: 25px;
            margin-bottom: 10px;
        }
        .id {
            color: #666666;
        }
        .time {
            color: #666666;
        }
    }
}
.login-info {
    p {
        line-height: 28px;
        font-size: 14px;
        color: #555555;
        span {
            color: #555555;
            margin-left: 80px;
        }
    }
}
.box-data {
    margin-top: 20px;
}
.box-game-data {
    margin-left: 160px;
    min-width: 880px;
    .scrollbar-demo-item {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 50px;
        margin: 10px;
        text-align: center;
        border-radius: 5px;
        background: var(--el-color-primary-light-9);
        color: var(--el-color-primary);
    }
    img {
        width: 60px;
        height: 40px;
    }
}
</style>
