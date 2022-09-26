<template>
    <div class="card register-title">
        <h1>注&nbsp;册</h1>
    </div>
    <div class="register-main card">
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
                    <button class="button is-dark" @click="test">注册</button>
                </div>
            </div>
        </el-form>
        <div class="back">
            <router-link to="/">返回</router-link>
        </div>
    </div>
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
.register-main {
    height: 16rem;
    width: 15rem;
    position: fixed;
    top: calc((100vh - 20rem) * 2 / 5);
    left: calc((100vw - 15rem) / 2);
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
    line-height: 40px;
    position: fixed;
    width: 15rem;
    padding-left: 2rem;
    padding-right: 2rem;
    padding-bottom: 0.6rem;
    padding-top: 0.6rem;
    left: calc((100vw - 15rem) / 2);
    top: calc((100vh - 25rem) * 2 / 5 - 40px);
    text-align: center;
    font-weight: lighter;
}
.register {
    margin-top: 1.5em;
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
