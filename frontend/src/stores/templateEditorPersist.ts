import type {
    ICardNode,
    IColumnNode,
    IAreaNode,
    IRowNode,
    IPropertyNode,
} from '@/trpg/card_template/Tree';
import CardTemplate from '@/trpg/card_template/CardTemplate';
import { defineStore } from 'pinia';
import { useTEStore } from './templateEditor';

export const useTEPStore = defineStore('templateEditor_persist', {
    state() {
        return {
            currentTemplate: new CardTemplate('', '', false, '', -1, '', ''),
        };
    },
    actions: {
        buildTemplate() {
            const tree = useTEStore().currentTree;
            const cardNode = tree[0] as ICardNode;
            const card = cardNode.card;
            card.columns = [];
            const cardChildren = cardNode.children;

            for (const i of cardChildren) {
                const columnNode = i as IColumnNode;
                const column = columnNode.column;
                column.areas = [];
                const columnChildren = columnNode.children;

                for (const j of columnChildren) {
                    const areaNode = j as IAreaNode;
                    const area = areaNode.area;
                    area.rows = [];
                    const areaChildren = areaNode.children;

                    for (const k of areaChildren) {
                        const rowNode = k as IRowNode;
                        const row = rowNode.row;
                        row.properties = [];
                        const rowChildren = rowNode.children;

                        for (const l of rowChildren) {
                            const propertyNode = l as IPropertyNode;
                            const property = propertyNode.property;
                            row.properties.push(property);
                        }

                        area.rows.push(row);
                    }

                    column.areas.push(area);
                }

                card.columns.push(column);
            }

            this.currentTemplate = card;
        },
    },
    persist: {
        enabled: true,
    },
});
