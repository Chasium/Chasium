<template>
    <div class="big-frame">
        <i class="fas fa-cog"></i>
        <div class="property-main">
            <div>{{ name }}</div>
            <el-input-number v-if="isNumProperty"></el-input-number>
            <el-input v-else-if="isStringProperty"></el-input>
            <el-select v-else-if="isSelectProperty"></el-select>
            <el-input v-else-if="isCalculatedProperty"></el-input>
            <el-avatar v-else-if="isImageProperty"></el-avatar>
            <el-button v-else-if="isButtonProperty"></el-button>
        </div>
        <i class="fas fa-trash-alt"></i>
    </div>
</template>

<script lang="ts">
import { PropertyType, type Property } from '@/trpg/card_template/Property';
import EvalScript from '@/trpg/script/EvalScript';
import { defineComponent } from 'vue';
export default defineComponent({
    props: {
        property: { type: Object, required: true },
    },
    computed: {
        propertyObj() {
            return this.property as Property;
        },
        isNumProperty() {
            const type = this.propertyObj.type;
            return type == PropertyType.INT || type == PropertyType.FLOAT;
        },
        isStringProperty() {
            return this.propertyObj.type == PropertyType.STRING;
        },
        isSelectProperty() {
            const type = this.propertyObj.type;
            return type == PropertyType.BOOL || type == PropertyType.SELECTION;
        },
        isCalculatedProperty() {
            const type = this.propertyObj.type;
            return (
                type == PropertyType.CALCULATED_INT ||
                type == PropertyType.CALCULATED_FLOAT ||
                type == PropertyType.CALCULATED_BOOL ||
                type == PropertyType.CALCULATED_STRING
            );
        },
        isImageProperty() {
            return this.propertyObj.type == PropertyType.IMAGE;
        },
        isButtonProperty() {
            return this.propertyObj.type == PropertyType.BUTTON;
        },
        name() {
            try {
                return new EvalScript(this.propertyObj.nameScript).run();
            } catch (e) {
                return '';
            }
        },
    },
});
</script>
