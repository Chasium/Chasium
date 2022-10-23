import CardTemplate from '@/trpg/card_template/CardTemplate';
import {
    NodeType,
    type IAreaNode,
    type ICardNode,
    type IColumnNode,
    type IPropertyNode,
    type IRowNode,
    type Tree,
} from '@/trpg/card_template/Tree';
import { defineStore } from 'pinia';
import { useTEPStore } from './templateEditorPersist';

export const useTEStore = defineStore('templateEditor', {
    state() {
        return {
            currentTree: [] as Tree[],
            currentTreeNodeId: 1000,
            currentColumnId: 0,
            currentAreaId: 0,
            currentRowId: 0,
            currentPropertyId: 0,
        };
    },
    actions: {
        buildTree() {
            this.currentTreeNodeId = 1000;
            const template = useTEPStore().currentTemplate;
            const root: ICardNode = {
                id: this.currentTreeNodeId,
                type: NodeType.CARD,
                label: '人物卡',
                card: new CardTemplate('', '', false, '', -1, '', ''),
                children: [],
                parent: undefined,
            };

            this.currentTreeNodeId++;

            for (const i of template.columns) {
                const column: IColumnNode = {
                    id: this.currentTreeNodeId,
                    type: NodeType.COLUMN,
                    label: `列${i.id}`,
                    column: i,
                    children: [],
                    parent: root,
                };

                if (i.id > this.currentColumnId) {
                    this.currentColumnId = i.id + 1;
                }

                this.currentTreeNodeId++;

                for (const j of i.areas) {
                    const area: IAreaNode = {
                        id: this.currentTreeNodeId,
                        type: NodeType.AREA,
                        label: `区域${j.id}`,
                        area: j,
                        children: [],
                        parent: column,
                    };

                    if (j.id > this.currentAreaId) {
                        this.currentAreaId = j.id + 1;
                    }

                    this.currentTreeNodeId++;

                    for (const k of j.rows) {
                        const row: IRowNode = {
                            id: this.currentTreeNodeId,
                            type: NodeType.ROW,
                            label: `行${k.id}`,
                            row: k,
                            children: [],
                            parent: area,
                        };

                        if (k.id > this.currentRowId) {
                            this.currentRowId = k.id + 1;
                        }

                        this.currentTreeNodeId++;

                        for (const l of k.properties) {
                            const property: IPropertyNode = {
                                id: this.currentTreeNodeId,
                                type: NodeType.PROPERTY,
                                label: `属性${l.id}`,
                                property: l,
                                children: [],
                                parent: row,
                            };

                            if (l.id > this.currentPropertyId) {
                                this.currentPropertyId = l.id + 1;
                            }

                            this.currentTreeNodeId++;

                            row.children.push(property);
                        }

                        area.children.push(row);
                    }

                    column.children.push(area);
                }

                root.children.push(column);
            }

            this.currentTree = [root];
        },
    },
});
