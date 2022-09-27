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
    <el-dialog
        draggable="true"
        v-model="createPropertyDialogVisible"
        title="创建属性"
    >
        <el-form>
            <el-form-item label="属性类型">
                <el-select v-model="nextPropertyType" placeholder="请选择">
                    <el-option
                        v-for="item in nextPropertyTypeOptions"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                    ></el-option>
                </el-select>
            </el-form-item>
            <el-row>
                <el-button type="primary" @click="confirmCreatePropertyDialog"
                    >确定</el-button
                >
                <el-button @click="cancelCreatePropertyDialog">取消</el-button>
            </el-row>
        </el-form>
    </el-dialog>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import type Node from 'element-plus/es/components/tree/src/model/node';
import { useTEStore } from '@/stores/templateEditor';
import type CardTemplate from '@/trpg/card_template/CardTemplate';
import { Column } from '@/trpg/card_template/Column';
import { Area, AreaType } from '@/trpg/card_template/Area';
import { Row } from '@/trpg/card_template/Row';
import {
    BoolProperty,
    ButtonProperty,
    ButtonPropertyPhase,
    CalculatedBoolProperty,
    CalculatedFloatProperty,
    CalculatedIntProperty,
    CalculatedStringProperty,
    FloatProperty,
    ImageProperty,
    IntProperty,
    PropertyType,
    SelectionProperty,
    StringProperty,
    type Property,
} from '@/trpg/card_template/Property';

// eslint抽风？？为什么
// eslint-disable-next-line no-unused-vars
enum NodeType {
    // eslint-disable-next-line no-unused-vars
    CARD,
    // eslint-disable-next-line no-unused-vars
    COLUMN,
    // eslint-disable-next-line no-unused-vars
    AREA,
    // eslint-disable-next-line no-unused-vars
    ROW,
    // eslint-disable-next-line no-unused-vars
    PROPERTY,
}

interface IBaseNode {
    id: number;
    type: NodeType;
    label: string;
    children: Tree[];
}

interface ICardNode extends IBaseNode {
    type: NodeType.CARD;
    card: CardTemplate;
}

interface IColumnNode extends IBaseNode {
    type: NodeType.COLUMN;
    column: Column;
}

interface IAreaNode extends IBaseNode {
    type: NodeType.AREA;
    area: Area;
}

interface IRowNode extends IBaseNode {
    type: NodeType.ROW;
    row: Row;
}

interface IPropertyNode extends IBaseNode {
    type: NodeType.PROPERTY;
    property: Property;
}

export type Tree =
    | ICardNode
    | IColumnNode
    | IAreaNode
    | IRowNode
    | IPropertyNode;

class Data {
    treeProps = {
        id: 'id',
        label: 'label',
        isLeaf: 'isLeaf',
    };
    nodeTypes = NodeType;
    createPropertyDialogVisible = false;
    nextPropertyType = PropertyType.INT;
    nextPropertyTypeOptions = [
        {
            value: PropertyType.INT,
            label: '玩家输入整数',
        },
        {
            value: PropertyType.FLOAT,
            label: '玩家输入浮点数',
        },
        {
            value: PropertyType.BOOL,
            label: '玩家输入布尔值',
        },
        {
            value: PropertyType.STRING,
            label: '玩家输入字符串',
        },
        {
            value: PropertyType.SELECTION,
            label: '选项字符串',
        },
        {
            value: PropertyType.CALCULATED_INT,
            label: '计算整数',
        },
        {
            value: PropertyType.CALCULATED_FLOAT,
            label: '计算浮点数',
        },
        {
            value: PropertyType.CALCULATED_BOOL,
            label: '计算布尔值',
        },
        {
            value: PropertyType.CALCULATED_STRING,
            label: '计算字符串',
        },
        {
            value: PropertyType.IMAGE,
            label: '图片',
        },
        {
            value: PropertyType.BUTTON,
            label: '按钮',
        },
    ];
    currentCreatingProperty?: IRowNode = undefined;
}

export default defineComponent({
    data() {
        return new Data();
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
            console.log(data);
            if (data.type == NodeType.CARD) {
                const column = new Column(
                    this.teStore.currentColumnId,
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
                });
                this.teStore.currentTreeNodeId++;
            } else if (data.type == NodeType.COLUMN) {
                const area = new Area(
                    this.teStore.currentAreaId,
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
                });
                this.teStore.currentTreeNodeId++;
            } else if (data.type == NodeType.ROW) {
                this.currentCreatingProperty = data;
                this.createPropertyDialogVisible = true;
            }
        },
        removeNode(node: Node, data: Tree) {
            const parent = node.parent;
            const parentData = parent.data as Tree;
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
        },
        editNode(data: Tree) {
            console.log(data);
        },
        confirmCreatePropertyDialog() {
            let property: Property = undefined as unknown as Property;
            if (this.nextPropertyType == PropertyType.INT) {
                property = new IntProperty(
                    this.teStore.currentPropertyId,
                    '',
                    false,
                    ''
                );
            } else if (this.nextPropertyType == PropertyType.FLOAT) {
                property = new FloatProperty(
                    this.teStore.currentPropertyId,
                    '',
                    '',
                    false,
                    ''
                );
            } else if (this.nextPropertyType == PropertyType.BOOL) {
                property = new BoolProperty(
                    this.teStore.currentPropertyId,
                    '',
                    false,
                    ''
                );
            } else if (this.nextPropertyType == PropertyType.STRING) {
                property = new StringProperty(
                    this.teStore.currentPropertyId,
                    '',
                    false,
                    ''
                );
            } else if (this.nextPropertyType == PropertyType.CALCULATED_INT) {
                property = new CalculatedIntProperty(
                    this.teStore.currentPropertyId,
                    '',
                    '',
                    false,
                    ''
                );
            } else if (this.nextPropertyType == PropertyType.CALCULATED_FLOAT) {
                property = new CalculatedFloatProperty(
                    this.teStore.currentPropertyId,
                    '',
                    '',
                    '',
                    false,
                    ''
                );
            } else if (this.nextPropertyType == PropertyType.CALCULATED_BOOL) {
                property = new CalculatedBoolProperty(
                    this.teStore.currentPropertyId,
                    '',
                    '',
                    false,
                    ''
                );
            } else if (
                this.nextPropertyType == PropertyType.CALCULATED_STRING
            ) {
                property = new CalculatedStringProperty(
                    this.teStore.currentPropertyId,
                    '',
                    '',
                    false,
                    ''
                );
            } else if (this.nextPropertyType == PropertyType.SELECTION) {
                property = new SelectionProperty(
                    this.teStore.currentPropertyId,
                    '',
                    '',
                    false,
                    ''
                );
            } else if (this.nextPropertyType == PropertyType.IMAGE) {
                property = new ImageProperty(
                    this.teStore.currentPropertyId,
                    ''
                );
            } else {
                property = new ButtonProperty(
                    this.teStore.currentPropertyId,
                    '',
                    ButtonPropertyPhase.ANY,
                    '',
                    ''
                );
            }
            this.teStore.currentPropertyId++;
            this.currentCreatingProperty?.row.properties.push(property);
            this.currentCreatingProperty?.children.push({
                type: NodeType.PROPERTY,
                id: this.teStore.currentTreeNodeId,
                label: `属性${property.id}`,
                property: property,
                children: [],
            });
            this.teStore.currentTreeNodeId++;
            this.createPropertyDialogVisible = false;
        },
        cancelCreatePropertyDialog() {
            this.createPropertyDialogVisible = false;
        },
    },
    mounted() {
        if (this.teStore.currentTree.length == 0) {
            this.teStore.currentTree = [
                {
                    id: this.teStore.currentTreeNodeId,
                    type: NodeType.CARD,
                    label: '人物卡',
                    card: this.teStore.currentTemplate,
                    children: [],
                },
            ];
            this.teStore.currentTreeNodeId++;
        }
    },
});
</script>
<style lang="scss" scoped>
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
