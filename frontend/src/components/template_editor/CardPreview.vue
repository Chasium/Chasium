<template>
    <div class="card-frame">
        <div class="card-content">
            <div class="column-container" v-for="item in nodeObj.children">
                <ColumnPreview
                    :column="item"
                    v-on:append-node="appendNode"
                    v-on:edit-node="editNode"
                    v-on:remove-node="removeNode"
                />
            </div>
            <div
                class="column-container add-column"
                @click="appendNode(nodeObj)"
            >
                <i class="fas fa-plus"></i>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import ColumnPreview from './ColumnPreview.vue';
import type { ICardNode, Tree } from '@/trpg/card_template/Tree';
import type Node from 'element-plus/es/components/tree/src/model/node';

export default defineComponent({
    props: {
        template: { type: Object, required: true },
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
    computed: {
        nodeObj() {
            return this.template as ICardNode;
        },
        cardObj() {
            return this.nodeObj.card;
        },
    },
    components: { ColumnPreview },
});
</script>

<style lang="scss" scoped>
@use '@/assets/css/card-colors.scss' as *;

.card-frame {
    width: 100%;
    height: 100%;
    overflow: scroll;
    border: 1px solid lightgray;
    border-radius: 4px;
    border-top-left-radius: 10px;

    &::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    &::-webkit-scrollbar-thumb {
        border-radius: 4px;
        background: rgba(0, 0, 0, 0.2);
    }

    &::-webkit-scrollbar-track {
        border-radius: 4px;
        background: rgba(0, 0, 0, 0.1);
    }
}

.card-content {
    display: flex;
    width: max-content;
}

.column-container {
    margin: 0.5em;
}

.add-column {
    color: $column-color;
    width: 10em;
    height: 20em;
    line-height: 20em;
    text-align: center;
    border: 2px dashed $column-color;
    border-radius: 10px;
    &:hover {
        border-color: $column-hover;
        i {
            color: $column-hover;
        }
    }
}
</style>
