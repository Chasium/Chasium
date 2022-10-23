<template>
    <div class="row-frame">
        <div class="title-col">
            <div class="row-title">{{ name }}</div>
            <i class="fas fa-cog" @click="editNode(nodeObj)"></i>
        </div>
        <div class="main-col">
            <div
                class="property-container"
                v-for="property in nodeObj.children"
            >
                <PropertyPreview
                    :property="property"
                    v-on:append-node="appendNode"
                    v-on:remove-node="removeNode"
                    v-on:edit-node="editNode"
                />
            </div>
            <div
                class="property-container add-property"
                @click="appendNode(nodeObj)"
            >
                <i class="fas fa-plus"></i>
            </div>
        </div>
        <i class="fas fa-trash-alt delete-row" @click="removeNode(nodeObj)"></i>
    </div>
</template>

<script lang="ts">
import EvalScript from '@/trpg/script/EvalScript';
import { defineComponent } from 'vue';
import PropertyPreview from './PropertyPreview.vue';
import type { IRowNode, Tree } from '@/trpg/card_template/Tree';

export default defineComponent({
    props: {
        row: { type: Object, required: true },
    },
    computed: {
        nodeObj() {
            return this.row as IRowNode;
        },
        rowObj() {
            return this.nodeObj.row;
        },
        name() {
            try {
                return new EvalScript(this.rowObj.nameScript).run();
            } catch (e) {
                return '';
            }
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
    methods: {
        appendNode(data: Tree) {
            this.$emit('appendNode', data);
        },
        removeNode(data: Tree) {
            this.$emit('removeNode', data);
        },
        editNode(data: Tree) {
            this.$emit('editNode', data);
        },
    },
    components: { PropertyPreview },
});
</script>

<style lang="scss" scoped>
@use '@/assets/css/card-colors.scss' as *;

.row-frame {
    border-radius: 6px;
    border: 1px solid $row-color;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

i {
    color: $row-color;
    &:hover {
        color: $row-hover;
    }
}

.title-col {
    display: flex;
    margin: 4px;
    align-items: center;
    i {
        line-height: 1.5em;
        margin-left: 2px;
    }
}

.row-title {
    min-width: 2em;
    min-height: 1.2em;
    line-height: 1.2em;
    border: 1px solid $row-hover;
    border-radius: 2px;
}

.main-col {
    flex-grow: 1;
    display: flex;
    align-items: center;
}

.property-container {
    margin: 4px;
}

.add-property {
    width: 5em;
    text-align: center;
    border: 2px dashed $property-color;
    border-radius: 6px;
    i {
        color: $property-color;
    }
    &:hover {
        border-color: $property-hover;
        i {
            color: $property-hover;
        }
    }
}

.delete-row {
    margin: 4px;
}
</style>
