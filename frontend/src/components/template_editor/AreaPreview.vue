<template>
    <div class="big-frame">
        <div class="title-area">
            <i class="fas fa-cog"></i>
            <div>{{}}</div>
        </div>
        <div class="main-area"></div>
    </div>
</template>

<script lang="ts">
import type { Area } from '@/trpg/card_template/Area';
import EvalScript from '@/trpg/script/EvalScript';
import { defineComponent } from 'vue';

export default defineComponent({
    props: {
        area: { type: Object, required: true },
    },
    computed: {
        areaObj() {
            return this.area as Area;
        },
        name() {
            try {
                return new EvalScript(this.areaObj.nameScript).run();
            } catch (e) {
                return '';
            }
        },
    },
});
</script>
