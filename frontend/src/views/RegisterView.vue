<template>
    <el-container>
        <div class="register-main card">
            <div class="register-title">注 册</div>
            <el-form label-width="75px" label-position="left">
                <el-form-item label="用户名:" class="user-data">
                    <input v-model="form.userName" placeholder="请输入用户名" />
                </el-form-item>
                <el-form-item label="密码:" class="user-data">
                    <input
                        type="password"
                        v-model="form.password"
                        show-password
                        placeholder="请输入密码"
                    />
                </el-form-item>
                <el-form-item label="确认密码:" class="user-data">
                    <input
                        type="password"
                        v-model="form.confirmPassword"
                        show-password
                        placeholder="请再次输入密码"
                    />
                </el-form-item>
                <div class="reminder" v-show="showReUser">
                    您输入用户名已被注册，请重新输入
                </div>
                <div class="reminder" v-show="showUser">用户名不能为空</div>
                <div class="reminder" v-show="showPass">密码不能为空</div>
                <div class="reminder" v-show="showUserWrong">用户名不合法</div>
                <div class="reminder" v-show="showPassWrong">密码不合法</div>
                <div class="reminder" v-show="showConfirmPass">请确认密码</div>
                <div class="reminder" v-show="showPassNotMatch">
                    两次输入密码不一致
                </div>
                <div class="register user-data">
                    <div class="container">
                        <a class="button is-dark" @click="createUser"> 注册 </a>
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
import axios from 'axios';
import type RegisterResponse from '@/generated/register/RegisterResponse';
import { useUserStore } from '@/stores/user';
import { defineComponent } from 'vue';

export default defineComponent({
    data() {
        return {
            showReUser: false,
            showUser: false,
            showPass: false,
            showConfirmPass: false,
            showPassNotMatch: false,
            showUserWrong: false,
            showPassWrong: false,
            form: {
                userName: '', //用户名
                password: '', //用户密码
                confirmPassword: '', //确认密码
            },
        };
    },
    computed: {
        userStore() {
            return useUserStore();
        },
    },
    methods: {
        async createUser() {
            this.showUser = false;
            this.showReUser = false;
            this.showPass = false;
            this.showConfirmPass = false;
            this.showPassNotMatch = false;
            if (this.form.userName == '') {
                this.showUser = true;
                return;
            } else if (this.form.password == '') {
                this.showPass = true;
                return;
            } else if (this.form.confirmPassword == '') {
                this.showConfirmPass = true;
                return;
            } else if (this.form.password != this.form.confirmPassword) {
                this.showPassNotMatch = true;
                return;
            }
            console.log(this.form.userName);
            try {
                let response = await axios.post<RegisterResponse>(
                    '/user/register',
                    {
                        userName: this.form.userName,
                        password: this.form.password,
                    }
                );
                this.showUserWrong = false;
                this.showReUser = false;
                this.showPassWrong = false;
                if (response.data['code'] === 0) {
                    alert('注册成功');
                    this.userStore.userName = this.form.userName;
                    this.$router.push('/login');
                } else if (response.data['code'] === 10) {
                    this.showUserWrong = true;
                    alert('用户名不合法');
                } else if (response.data['code'] === 11) {
                    this.showReUser = true;
                    alert('用户已存在');
                } else if (response.data['code'] === 20) {
                    this.showPassWrong = true;
                    alert('密码不合法');
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
.register-main {
    height: 22rem;
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
    margin-top: 2.5em;
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
    margin-bottom: 1.5em;
}
.back {
    width: 100%;
    text-align: end;
}
</style>
