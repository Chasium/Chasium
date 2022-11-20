<template>
    <el-container>
        <el-header class="title">Chasium 在线TRPG平台</el-header>
        <div class="login-main card">
            <div class="login-title">登 录</div>
            <el-form>
                <el-form-item class="user-data">
                    <input
                        v-model="form.userName"
                        placeholder="用户名"
                        class="input_data"
                    />
                </el-form-item>
                <el-form-item class="user-data">
                    <input
                        type="password"
                        v-model="form.password"
                        show-password
                        placeholder="密码"
                    />
                </el-form-item>
                <div class="reminder" v-show="showUser">用户名不能为空</div>
                <div class="reminder" v-show="showPass">密码不能为空</div>
                <div class="reminder" v-show="showUserWrong">用户名不存在</div>
                <div class="reminder" v-show="showPassWrong">密码错误</div>
                <div class="login user-data">
                    <div class="container">
                        <a class="button is-dark" @click="login"> 登录 </a>
                    </div>
                </div>
            </el-form>
            <div class="create-user">
                <router-link to="/register">注册新账户</router-link>
            </div>
        </div>
    </el-container>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';
import type LoginResponse from '@/generated/login/LoginResponse';
import { useUserStore } from '@/stores/user';
import { stringLiteral } from '@babel/types';

export default defineComponent({
    data() {
        return {
            showUser: false,
            showPass: false,
            showUserWrong: false,
            showPassWrong: false,
            form: {
                userName: '', //用户名
                password: '', //用户密码
            },
        };
    },
    computed: {
        userStore() {
            return useUserStore();
        },
    },
    methods: {
        async login() {
            this.showPass = false;
            this.showUser = false;
            if (this.form.userName == '') {
                this.showUser = true;
                return;
            } else if (this.form.password == '') {
                this.showPass = true;
                this.showUser = false;
                return;
            }
            console.log(this.form.userName);
            try {
                let response = await axios.post<LoginResponse>('/user/login', {
                    userName: this.form.userName,
                    password: this.form.password,
                });
                this.showUserWrong = false;
                this.showPassWrong = false;
                if (
                    response.data['code'] === 0 ||
                    response.data['code'] === 3
                ) {
                    // alert('登录成功');
                    //TODO：跳转到主页面
                    this.userStore.userName = this.form.userName;
                    this.userStore.session = response.data['session'];
                    console.log('user session: ' + this.userStore.session);
                    this.userStore.loggedIn = true;
                    // this.$router.push('/chat');
                    this.$router.push('/lobby');
                } else if (response.data['code'] === 1) {
                    this.showUserWrong = true;
                    this.userStore.loggedIn = false;
                    alert('用户名不存在');
                } else if (response.data['code'] === 2) {
                    this.showPassWrong = true;
                    this.userStore.loggedIn = false;
                    alert('密码错误');
                } else {
                    alert('未知错误');
                }
            } catch (err) {
                alert('异常');
            }
        },
    },
});
</script>

<style lang="scss" scoped>
@import 'bulma/bulma.sass';

.el-container {
    height: 100vh;
    width: 100vw;
    font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB',
        'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
}
.title {
    text-align: center;
    padding-top: calc((100vh - 20rem) * 3 / 7 - 2.5em);
    font-size: 45px;
}
.login-main {
    height: 20rem;
    width: 15rem;
    position: fixed;
    top: calc((100vh - 20rem) * 3 / 7);
    padding: 2rem;
    left: 50%;
    transform: translate(-50%, 0);

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
    padding-bottom: 2rem;
    text-align: center;
    font-weight: lighter;
}

.login {
    margin-top: 3em;
    .container {
        width: fit-content;
        a.button {
            height: 1.5em;
            width: 10em;
        }
    }
}
.reminder {
    font-size: small;
    text-align: center;
    color: crimson;
    line-height: 0.1em;
}
.user-data {
    margin-bottom: 2em;
}
.create-user {
    width: 100%;
    text-align: end;
    margin-top: 2em;
}
</style>
