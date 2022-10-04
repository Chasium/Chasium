import type { Tree } from '@/components/template_editor/TemplateEditorAside.vue';
import CardTemplate from '@/trpg/card_template/CardTemplate';
import { defineStore } from 'pinia';

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
});
