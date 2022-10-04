<template>
    <div class="property-frame">
        <i class="fas fa-cog" @click="$emit('editNode', nodeObj)"></i>
        <div class="main-col">
            <div class="property-title">{{ name }}</div>
            <div class="property-main el-color-change">
                <el-input-number
                    size="small"
                    readonly
                    v-if="isNumProperty"
                ></el-input-number>
                <el-input
                    size="small"
                    readonly
                    v-else-if="isStringProperty"
                ></el-input>
                <el-select
                    size="small"
                    readonly
                    v-else-if="isSelectProperty"
                ></el-select>
                <el-input
                    size="small"
                    readonly
                    v-else-if="isCalculatedProperty"
                ></el-input>
                <el-avatar
                    shape="square"
                    v-else-if="isImageProperty"
                ></el-avatar>
                <el-button
                    v-else-if="isButtonProperty"
                    size="small"
                    class="button-property el-color-change"
                    >{{ buttonText }}</el-button
                >
            </div>
        </div>
        <i class="fas fa-trash-alt" @click="$emit('removeNode', nodeObj)"></i>
    </div>
</template>

<script lang="ts">
import { PropertyType } from '@/trpg/card_template/Property';
import EvalScript from '@/trpg/script/EvalScript';
import { defineComponent } from 'vue';
import type { IPropertyNode, Tree } from '@/trpg/card_template/Tree';

export default defineComponent({
    props: {
        property: { type: Object, required: true },
    },
    computed: {
        nodeObj() {
            return this.property as IPropertyNode;
        },
        propertyObj() {
            return this.nodeObj.property;
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
        buttonText() {
            if (this.propertyObj.type == PropertyType.BUTTON) {
                return new EvalScript(this.propertyObj.textScript).run();
            }
            return '';
        },
    },
    emits: {
        appendNode(data: Tree) {
            return true;
        },
        removeNode(data: Tree) {
            return true;
        },
        editNode(data: Tree) {
            return true;
        },
    },
});
</script>

<style lang="scss" scoped>
@use '@/assets/css/card-colors.scss' as *;

.property-frame {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border: 1px solid $property-color;
    border-radius: 4px;
}

i {
    color: $property-color;
    margin: 4px;
    &:hover {
        color: $property-hover;
    }
}

.main-col {
    width: min-content;
}

.property-title {
    margin: 2px;
    min-width: 3em;
    min-height: 1.2em;
    line-height: 1.2em;
    border: 1px solid $property-hover;
    border-radius: 2px;
}

.property-main {
    margin: 2px;
    display: flex;
    justify-content: center;
}

.el-color-change {
    --el-fill-color-light: #{$property-el-color};
    --el-color-primary: #{$property-hover};
    --el-button-hover-border-color: #{$property-hover};
    --el-button-hover-bg-color: #{$property-el-color};
    --el-input-border-color: #{$property-color};
    $lighter-property-color: rgba($property-color, 75%);
    --el-border-color: #{$lighter-property-color};
    --el-text-color-disabled: #{$lighter-property-color};
    --el-input-hover-border-color: #{$property-hover};
    --el-button-hover-border-color: #{$property-hover};
    --el-button-hover-bg-color: #{rgba($property-hover, 50%)};
    --el-button-bg-color: #{rgba($property-hover, 25%)};
}

.button-property {
    min-width: 3em;
}
</style>
