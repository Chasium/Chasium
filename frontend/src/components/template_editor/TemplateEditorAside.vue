<template>
    <div class="aside-main">
        <el-tree
            class="tree"
            :props="treeProps"
            :data="teStore.currentTree"
            default-expand-all
            :expand-on-click-node="false"
        >
            <template #default="{ node, data }">
                <span class="tree-node">
                    <i
                        v-if="data.type == nodeTypes.CARD"
                        class="fas fa-file"
                    ></i>
                    <i
                        v-if="data.type == nodeTypes.COLUMN"
                        class="fas fa-columns"
                    ></i>
                    <i
                        v-if="data.type == nodeTypes.AREA"
                        class="fas fa-file-alt"
                    ></i>
                    <i
                        v-if="data.type == nodeTypes.ROW"
                        class="fas fa-bars"
                    ></i>
                    <i
                        v-if="data.type == nodeTypes.PROPERTY"
                        class="fas fa-table"
                    ></i>
                    <span>{{ node.label }}</span>
                    <span>
                        <a
                            v-if="data.type != nodeTypes.PROPERTY"
                            @click="appendNode(data)"
                            >{{ appendText(data) }}</a
                        >
                        <a
                            v-if="data.type != nodeTypes.CARD"
                            @click="removeNode(node, data)"
                            >删除</a
                        >
                        <a @click="editNode(data)">编辑</a>
                    </span>
                </span>
            </template>
        </el-tree>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import type Node from 'element-plus/es/components/tree/src/model/node';
import { useTEStore } from '@/stores/templateEditor';
import CardTemplate from '@/trpg/card_template/CardTemplate';
import type { Column } from '@/trpg/card_template/Column';
import type { Area } from '@/trpg/card_template/Area';
import type { Row } from '@/trpg/card_template/Row';
import type { Property } from '@/trpg/card_template/Property';
import { NodeType, type Tree } from '@/trpg/card_template/Tree';

class Data {
    treeProps = {
        id: 'id',
        label: 'label',
        isLeaf: 'isLeaf',
    };
    nodeTypes = NodeType;
}

export default defineComponent({
    data() {
        return new Data();
    },
    emits: {
        appendNode(__data: Tree) {
            return true;
        },
        removeNode(__data: Tree) {
            return true;
        },
        editNode(__data: Tree) {
            return true;
        },
    },
    computed: {
        teStore() {
            return useTEStore();
        },
        appendText() {
            return function (data: Tree) {
                switch (data.type) {
                    case NodeType.CARD:
                        return '添加列';
                    case NodeType.COLUMN:
                        return '添加区域';
                    case NodeType.AREA:
                        return '添加行';
                    case NodeType.ROW:
                        return '添加属性';
                    default:
                        return '';
                }
            };
        },
    },
    methods: {
        appendNode(data: Tree) {
            this.$emit('appendNode', data);
        },
        removeNode(__node: Node, data: Tree) {
            this.$emit('removeNode', data);
        },
        editNode(data: Tree) {
            this.$emit('editNode', data);
        },
    },
});
</script>
<style lang="scss" scoped>
@use '@/assets/css/card-colors.scss' as *;

.aside-main {
    width: 100%;
    height: 100%;
    overflow: scroll;

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
.tree {
    margin-top: 1em;
}

.tree-node {
    i {
        margin-right: 0.25em;
        &.fa-columns {
            color: $column-color;
        }
        &.fa-file-alt {
            color: $area-color;
        }
        &.fa-bars {
            color: $row-color;
        }
        &.fa-table {
            color: $property-color;
        }
    }
    span {
        margin-right: 0.5em;
    }
    a {
        text-decoration: underline;
        margin-right: 0.5em;
        &:hover {
            color: lightgray;
        }
    }
}
</style>
