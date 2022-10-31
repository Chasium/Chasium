<template>
    <el-container>
        <el-header>Logout</el-header>
    </el-container>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useUserStore } from '@/stores/user';
import type LogoutResponse from '@/generated/logout/LogoutResponse';
import axios from 'axios';

export default defineComponent({
    data() {
        return {
            data: {},
        };
    },
    computed: {
        userStore() {
            return useUserStore();
        },
    },
    methods: {
        async logout() {
            if (this.userStore.session != '') {
                let response = await axios.post<LogoutResponse>(
                    '/user/logout',
                    {
                        userName: this.userStore.userName,
                        session: this.userStore.session,
                    }
                );
                if (response.data['code'] === 0) {
                    alert('user ' + response.data['userName'] + ' logout!');
                } else {
                    alert('error');
                }
            } else {
                alert('No logged!');
            }
            this.$router.push('/');
        },
    },
    mounted() {
        this.logout();
    },
});
</script>
