<template>
    <div>
        <p>Room ID: {{ roomID }}</p>
        <button @click="$emit('joinRoom')">join</button>
    </div>
</template>
<script>
import { defineComponent } from 'vue';
export default defineComponent({
    props: {
        roomID: Number,
    },
});
</script>
