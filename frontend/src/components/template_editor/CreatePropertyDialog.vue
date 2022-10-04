<template>
    <el-dialog draggable v-model="visible" width="30%" title="创建属性">
        <template #default>
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
            </el-form>
        </template>
        <template #footer>
            <el-button type="primary" @click="confirm">确定</el-button>
            <el-button @click="cancel">取消</el-button>
        </template>
    </el-dialog>
</template>

<script lang="ts">
import { useTEStore } from '@/stores/templateEditor';
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
import { defineComponent } from 'vue';
import { NodeType, type IRowNode } from '@/trpg/card_template/Tree';

class Data {
    visible = false;
    currentCreatingProperty?: IRowNode = undefined;
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
}

export default defineComponent({
    data() {
        return new Data();
    },
    computed: {
        teStore() {
            return useTEStore();
        },
    },
    emits: ['cardEdit'],
    methods: {
        show(node: IRowNode) {
            this.currentCreatingProperty = node;
            this.visible = true;
        },
        confirm() {
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
                parent: this.currentCreatingProperty,
            });
            this.teStore.currentTreeNodeId++;
            this.visible = false;

            this.$emit('cardEdit');
        },
        cancel() {
            this.visible = false;
        },
    },
});
</script>
