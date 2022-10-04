<template>
    <div class="column-frame">
        <div class="title-row">
            <i class="fas fa-cog" @click="editNode(nodeObj)"></i>
            <div class="column-title">{{ name }}</div>
            <i class="fas fa-trash-alt" @click="removeNode(nodeObj)"></i>
        </div>
        <div class="main-row">
            <div class="area-container" v-for="item in nodeObj.children">
                <AreaPreview
                    :area="item"
                    v-on:append-node="appendNode"
                    v-on:edit-node="editNode"
                    v-on:remove-node="removeNode"
                />
            </div>
            <div class="add-area area-container" @click="appendNode(nodeObj)">
                <i class="fas fa-plus"></i>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import EvalScript from '@/trpg/script/EvalScript';
import { defineComponent } from 'vue';
import AreaPreview from './AreaPreview.vue';
import type { IColumnNode, Tree } from '@/trpg/card_template/Tree';

export default defineComponent({
    props: {
        column: { type: Object, required: true },
    },
    computed: {
        nodeObj() {
            return this.column as IColumnNode;
        },
        columnObj() {
            return this.nodeObj.column;
        },
        name() {
            try {
                return new EvalScript(this.columnObj.nameScript).run();
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
    components: { AreaPreview },
});
</script>

<style lang="scss" scoped>
@use '@/assets/css/card-colors.scss' as *;

.column-frame {
    border-radius: 10px;
    border: 1px solid $column-color;
    min-width: 10em;
}

.column-title {
    min-width: 2em;
    min-height: 1.2em;
    line-height: 1.2em;
    margin-left: 5px;
    margin-right: 5px;
    border: 1px solid $column-hover;
    border-radius: 2px;
}

i {
    color: $column-color;
    &:hover {
        color: $column-hover;
    }
}

.title-row {
    display: flex;
    align-items: center;
    margin-left: 5px;
    margin-right: 5px;
    margin-top: 5px;
    margin-bottom: 2px;
    justify-content: space-between;
}

.main-row {
    display: inline;
}

.area-container {
    margin: 5px;
}

.add-area {
    height: 5em;
    text-align: center;
    line-height: 5em;
    border: 2px dashed $area-color;
    border-radius: 10px;
    i {
        color: $area-color;
    }
    &:hover {
        border-color: $area-hover;
        i {
            color: $area-hover;
        }
    }
}
</style>
