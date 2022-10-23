<template>
    <el-container class="big-frame">
        <el-header class="editor-header" height="2em">test header</el-header>
        <el-main class="editor-frame">
            <el-container class="editor-container">
                <el-aside width="20em" class="editor-aside">
                    <TemplateEditorAside
                        v-on:append-node="appendNode"
                        v-on:remove-node="removeNode"
                        v-on:edit-node="editNode"
                    />
                </el-aside>
                <el-main class="editor-main">
                    <CardPreview
                        :template="currentTemplate"
                        v-on:append-node="appendNode"
                        v-on:remove-node="removeNode"
                        v-on:edit-node="editNode"
                    />
                </el-main>
            </el-container>
        </el-main>
    </el-container>
    <CreatePropertyDialog
        ref="create-property-dialog"
        v-on:card-edit="onCardEdit"
    />
</template>

<script lang="ts">
import { useTEStore } from '@/stores/templateEditor';
import { defineComponent } from 'vue';
import TemplateEditorAside from '../components/template_editor/TemplateEditorAside.vue';
import CardPreview from '../components/template_editor/CardPreview.vue';
import { Area, AreaType } from '@/trpg/card_template/Area';
import { Column } from '@/trpg/card_template/Column';
import type { Property } from '@/trpg/card_template/Property';
import { Row } from '@/trpg/card_template/Row';
import CreatePropertyDialog from '../components/template_editor/CreatePropertyDialog.vue';
import { refHelper } from '@/utils/refHelper';
import { type ICardNode, type Tree, NodeType } from '@/trpg/card_template/Tree';
import { create, property } from 'lodash';
import { useTEPStore } from '@/stores/templateEditorPersist';

class Data {
    currentTemplate: ICardNode = {
        ...useTEStore().currentTree[0],
    } as ICardNode;
}

export default defineComponent({
    data() {
        return new Data();
    },
    computed: {
        teStore() {
            return useTEStore();
        },
        tepStore() {
            return useTEPStore();
        },
        createPropertyDialog() {
            return refHelper(
                this,
                'create-property-dialog',
                CreatePropertyDialog
            );
        },
    },
    components: { TemplateEditorAside, CardPreview, CreatePropertyDialog },
    methods: {
        onCardEdit() {
            this.tepStore.buildTemplate();
            this.currentTemplate = {
                ...useTEStore().currentTree[0],
            } as ICardNode;
        },
        appendNode(data: Tree) {
            console.log(data);
            if (data.type == NodeType.CARD) {
                const column = new Column(
                    this.teStore.currentColumnId,
                    '',
                    false,
                    ''
                );
                this.teStore.currentColumnId++;
                data.card.columns.push(column);
                data.children.push({
                    type: NodeType.COLUMN,
                    id: this.teStore.currentTreeNodeId,
                    label: `列${column.id}`,
                    column: column,
                    children: [],
                    parent: data,
                });
                this.teStore.currentTreeNodeId++;
            } else if (data.type == NodeType.COLUMN) {
                const area = new Area(
                    this.teStore.currentAreaId,
                    '',
                    AreaType.PERMANENT,
                    false,
                    '',
                    false
                );
                this.teStore.currentAreaId++;
                data.column.areas.push(area);
                data.children.push({
                    type: NodeType.AREA,
                    id: this.teStore.currentTreeNodeId,
                    label: `区域${area.id}`,
                    area: area,
                    children: [],
                    parent: data,
                });
                this.teStore.currentTreeNodeId++;
            } else if (data.type == NodeType.AREA) {
                const row = new Row(this.teStore.currentRowId, '', false, '');
                this.teStore.currentRowId++;
                data.area.rows.push(row);
                data.children.push({
                    type: NodeType.ROW,
                    id: this.teStore.currentTreeNodeId,
                    label: `行${row.id}`,
                    row: row,
                    children: [],
                    parent: data,
                });
                this.teStore.currentTreeNodeId++;
            } else if (data.type == NodeType.ROW) {
                this.createPropertyDialog.show(data);
            }

            if (data.type != NodeType.ROW) {
                this.onCardEdit();
            }
        },
        removeNode(data: Tree) {
            if (data.type == NodeType.CARD) {
                return;
            }
            const parentData = data.parent;
            if (
                parentData.type == NodeType.CARD &&
                data.type == NodeType.COLUMN
            ) {
                const children: Column[] = parentData.card.columns;
                const index = children.findIndex(
                    (d) => d.id === data.column.id
                );
                children.splice(index, 1);
            } else if (
                parentData.type == NodeType.COLUMN &&
                data.type == NodeType.AREA
            ) {
                const children: Area[] = parentData.column.areas;
                const index = children.findIndex((d) => d.id === data.area.id);
                children.splice(index, 1);
            } else if (
                parentData.type == NodeType.AREA &&
                data.type == NodeType.ROW
            ) {
                const children: Row[] = parentData.area.rows;
                const index = children.findIndex((d) => d.id === data.row.id);
                children.splice(index, 1);
            } else if (
                parentData.type == NodeType.ROW &&
                data.type == NodeType.PROPERTY
            ) {
                const children: Property[] = parentData.row.properties;
                const index = children.findIndex(
                    (d) => d.id === data.property.id
                );
                children.splice(index, 1);
            }
            const children: Tree[] = parentData.children;
            const index = children.findIndex((d) => d.id === data.id);
            children.splice(index, 1);

            this.onCardEdit();
        },
        editNode(data: Tree) {
            console.log(data);
        },
    },
    mounted() {
        if (this.teStore.currentTree.length == 0) {
            this.teStore.buildTree();
            this.currentTemplate = {
                ...useTEStore().currentTree[0],
            } as ICardNode;
        }
    },
});
</script>

<style lang="scss" scoped>
.big-frame {
    position: fixed;
    width: 100vw;
    height: 100vh;
}

.editor-header {
    background-color: gray;
}

.editor-frame {
    padding: 0px;
    height: calc(100% - 2em);
}

.editor-container {
    width: 100%;
    height: 100%;
}

.editor-main {
    padding: 1em;
    overflow: hidden;
}

.editor-aside {
    box-shadow: 3px 0 3px gray;
}
</style>
