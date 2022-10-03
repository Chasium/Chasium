<template>
    <div class="big-frame">
        <div>{{ name }}</div>
        <i class="fas fa-cog"></i>
        <div class="properties">
            <div
                class="property-container"
                v-for="property in rowObj.properties"
            >
                <PropertyPreview :property="property"></PropertyPreview>
            </div>
        </div>
        <a class="add-property"><i class="fas fa-plus"></i></a>
        <i class="fas fa-trash-alt"></i>
    </div>
</template>

<script lang="ts">
import type { Row } from '@/trpg/card_template/Row';
import EvalScript from '@/trpg/script/EvalScript';
import { defineComponent } from 'vue';
import PropertyPreview from './PropertyPreview.vue';

export default defineComponent({
    props: {
        row: { type: Object, required: true },
    },
    computed: {
        rowObj() {
            return this.row as Row;
        },
        name() {
            try {
                return new EvalScript(this.rowObj.nameScript).run();
            } catch (e) {
                return '';
            }
        },
    },
    components: { PropertyPreview },
});
</script>
