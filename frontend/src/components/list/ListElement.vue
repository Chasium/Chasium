<template>
    <div class="big-frame" :style="frameSize">
        <div class="image">
            <img :src="image" />
        </div>
        <div class="name">
            <a @click="$emit('nameClick', item)">{{ name }}</a>
        </div>
        <div class="description">{{ description }}</div>
    </div>
</template>

<script lang="ts">
import { defineComponent, type StyleValue } from 'vue';

export default defineComponent({
    props: {
        width: String,
        height: String,
        image: String,
        item: {
            type: Object,
            required: true,
        },
        name: {
            type: String,
            required: true,
        },
        description: String,
    },
    emits: {
        nameClick(item: any) {
            return true;
        },
    },
    computed: {
        frameSize(): StyleValue {
            return {
                width: this.width == null ? '120px' : this.width,
                height: this.height == null ? '180px' : this.height,
            };
        },
    },
});
</script>

<style lang="scss" scoped>
.image {
    height: 60%;
    width: 100%;
}

.description {
    overflow: hidden;
}
</style>
