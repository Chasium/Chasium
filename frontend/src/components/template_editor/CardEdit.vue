<template>
    <el-form label-width="15em">
        <el-form-item label="模板名称">
            <el-input v-model="name"></el-input>
        </el-form-item>
        <el-form-item label="模板描述">
            <el-input v-model="description"></el-input>
        </el-form-item>
        <el-form-item label="是否需要检验">
            <el-switch v-model="needCheck"></el-switch>
        </el-form-item>
        <el-form-item label="检验脚本">
            <el-button>编辑</el-button>
        </el-form-item>
        <el-form-item label="用作封面的属性id">
            <el-input-number v-model="coverPropertyId"></el-input-number>
        </el-form-item>
        <el-form-item label="人物卡描述生成脚本">
            <el-button>编辑</el-button>
        </el-form-item>
        <el-form-item label="游戏内人物卡预览生成脚本">
            <el-button>编辑</el-button>
        </el-form-item>
        <el-row>
            <el-button @click="close(true)">确定</el-button>
            <el-button @click="close(false)">取消</el-button>
        </el-row>
    </el-form>
</template>

<script lang="ts">
import { NodeType, type Tree } from '@/trpg/card_template/Tree';
import { defineComponent } from 'vue';

class Data {
    name = '';
    description = '';
    needCheck = false;
    checkScript = '';
    coverPropertyId = -1;
    cardDescriptionScript = '';
    inGameCardScript = '';
    currentNode?: Tree = undefined;
}

export default defineComponent({
    data() {
        return new Data();
    },
    emits: ['close'],
    methods: {
        open(node: Tree) {
            this.currentNode = node;
            if (node.type == NodeType.CARD) {
                const card = node.card;
                this.name = card.name;
                this.description = card.description;
                this.needCheck = card.needCheck;
                this.checkScript = card.checkScript;
                this.coverPropertyId = card.coverPropertyId;
                this.cardDescriptionScript = card.cardDescriptionScript;
                this.inGameCardScript = card.inGameCardScript;
            }
        },
        close(save: boolean) {
            if (
                save &&
                this.currentNode &&
                this.currentNode.type == NodeType.CARD
            ) {
                const card = this.currentNode.card;
                card.name = this.name;
                card.description = this.description;
                card.needCheck = this.needCheck;
                card.checkScript = this.checkScript;
                card.coverPropertyId = this.coverPropertyId;
                card.cardDescriptionScript = this.cardDescriptionScript;
                card.inGameCardScript = this.inGameCardScript;
            }
            this.$emit('close');
        },
    },
});
</script>
