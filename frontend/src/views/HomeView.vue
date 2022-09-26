<template>
    <div class="background">
        <div class="login-title card">
            <h1>登&nbsp;录</h1>
        </div>
        <div class="login-main card">
            <el-form>
                <el-form-item class="user-data">
                    <input
                        v-model="userName"
                        placeholder="用户名"
                        class="input_data"
                    />
                </el-form-item>
                <el-form-item class="user-data">
                    <input
                        type="password"
                        v-model="password"
                        show-password
                        placeholder="密码"
                    />
                </el-form-item>
                <div class="login user-data">
                    <div class="container">
                        <button class="button is-dark" @click="test">
                            登录
                        </button>
                    </div>
                </div>
            </el-form>
            <div class="create-user">
                <router-link to="/register">注册新账户</router-link>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

class Data {
    userName: string = '';
    password: string = '';
}

export default defineComponent({
    data() {
        return new Data();
    },
    methods: {
        test() {
            console.log(this.userName);
        },
    },
});
</script>

<style lang="scss" scoped>
@import 'bulma/bulma.sass';
.background {
    width: 100vw;
    height: 100vh;
}
.login-main {
    height: 16rem;
    width: 15rem;
    position: fixed;
    top: calc((100vh - 20rem) * 2 / 5);
    left: calc((100vw - 15rem) / 2);
    padding: 2rem;

    input {
        width: 100%;
        border: none;
        border-bottom: 2px solid silver;
        outline: none;
        font-size: 16px;
    }
}
.login-title {
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

.login {
    margin-top: 3em;
    .container {
        width: fit-content;
        button {
            height: 1.5em;
            width: 10em;
        }
    }
}
.user-data {
    margin-bottom: 2em;
}
.create-user {
    width: 100%;
    text-align: end;
    margin-top: 3em;
}
</style>
