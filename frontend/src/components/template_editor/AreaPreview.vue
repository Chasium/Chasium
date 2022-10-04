<template>
    <div class="area-frame">
        <div class="title-row">
            <i class="fas fa-cog" @click="editNode(nodeObj)"></i>
            <div class="area-title">{{ name }}</div>
            <i class="fas fa-trash-alt" @click="removeNode(nodeObj)"></i>
        </div>
        <div class="main-row">
            <div class="row-container" v-for="item in nodeObj.children">
                <RowPreview
                    :row="item"
                    v-on:append-node="appendNode"
                    v-on:edit-node="editNode"
                    v-on:remove-node="removeNode"
                />
            </div>
            <div class="row-container add-row" @click="appendNode(nodeObj)">
                <i class="fas fa-plus"></i>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import EvalScript from '@/trpg/script/EvalScript';
import { defineComponent } from 'vue';
import RowPreview from './RowPreview.vue';
import type { IAreaNode, Tree } from '@/trpg/card_template/Tree';

export default defineComponent({
    props: {
        area: { type: Object, required: true },
    },
    computed: {
        nodeObj() {
            return this.area as IAreaNode;
        },
        areaObj() {
            return this.nodeObj.area;
        },
        name() {
            try {
                return new EvalScript(this.areaObj.nameScript).run();
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
    components: { RowPreview },
});
</script>

<style lang="scss" scoped>
@use '@/assets/css/card-colors.scss' as *;

.area-frame {
    border-radius: 8px;
    border: 1px solid $area-color;
}

.area-title {
    min-width: 2em;
    min-height: 1.2em;
    line-height: 1.2em;
    margin-left: 4px;
    margin-right: 4px;
    border: 1px solid $area-hover;
    border-radius: 2px;
}

i {
    color: $area-color;
    &:hover {
        color: $area-hover;
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

.row-container {
    margin: 4px;
}

.add-row {
    text-align: center;
    border: 2px dashed $row-color;
    border-radius: 8px;
    i {
        color: $row-color;
    }
    &:hover {
        border-color: $row-hover;
        i {
            color: $row-hover;
        }
    }
}
</style>
