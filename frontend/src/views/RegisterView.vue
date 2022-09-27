<template>
    <el-container>
        <div class="register-main card">
            <div class="register-title">注 册</div>
            <el-form label-width="75px" label-position="left">
                <el-form-item label="用户名:" class="user-data">
                    <input v-model="userName" placeholder="请输入用户名" />
                </el-form-item>
                <el-form-item label="密码:" class="user-data">
                    <input
                        type="password"
                        v-model="password"
                        show-password
                        placeholder="请输入密码"
                    />
                </el-form-item>
                <el-form-item label="确认密码:" class="user-data">
                    <input
                        type="password"
                        v-model="confirmPassword"
                        show-password
                        placeholder="请再次输入密码"
                    />
                </el-form-item>
                <div class="register user-data">
                    <div class="container">
                        <button class="button is-dark" @click="test">
                            注册
                        </button>
                    </div>
                </div>
            </el-form>
            <div class="back">
                <router-link to="/">返回</router-link>
            </div>
        </div>
    </el-container>
</template>

<script lang="ts">
class Data {
    userName: string = '';
    password: string = '';
    confirmPassword: string = '';
}

export default {
    data() {
        return new Data();
    },
};
</script>

<style lang="scss" scoped>
@import 'bulma/bulma.sass';
.el-container {
    height: 100vh;
    width: 100vw;
    font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB',
        'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
}
.register-main {
    height: 20rem;
    width: 15rem;
    position: fixed;
    top: calc((100vh - 20rem) * 3 / 7);
    left: 50%;
    transform: translate(-50%, 0);
    padding: 2rem;

    input {
        border: none;
        border-bottom: 2px solid silver;
        outline: none;
        font-size: 14px;
    }
}
.register-title {
    font-size: 36px;
    padding-bottom: 1.5rem;
    text-align: center;
    font-weight: lighter;
}
.register {
    margin-top: 2em;
    .container {
        width: fit-content;
        button {
            height: 1.5em;
            width: 10em;
        }
    }
}
.user-data {
    margin-bottom: 1.5em;
}
.back {
    width: 100%;
    text-align: end;
}
</style>
