<template>
    <div class="big-frame">
        <div v-for="lineId in currentList.length / _perLine">
            <el-row>
                <div v-for="lineItemId in lineItems(lineId)">
                    <ListElement
                        :item="item(lineId, lineItemId)"
                        :name="_list.getName(item(lineId, lineItemId))"
                        :description="
                            _list.getDescription(item(lineId, lineItemId))
                        "
                        :image="_list.getImage(item(lineId, lineItemId))"
                        :width="elementWidth"
                        :height="elementHeight"
                        @name-click="(item) => _list.onItemClick(item)"
                    />
                </div>
            </el-row>
        </div>
    </div>
</template>

<script lang="ts">
import { BaseListObject, ListObject } from '@/component_logics/ListObject';
import { defineComponent } from 'vue';
import ListElement from './ListElement.vue';

class Data {
    currentList: any[] = [];
}

export default defineComponent({
    props: {
        list: {
            type: BaseListObject,
            required: true,
        },
        perLine: Number,
        perPage: Number,
        elementWidth: String,
        elementHeight: String,
    },
    data() {
        return new Data();
    },
    computed: {
        _perLine() {
            return this.perLine == null ? 5 : this.perLine;
        },
        _perPage() {
            return this.perPage == null ? 20 : this.perPage;
        },
        _list() {
            return this.list as ListObject;
        },
    },
    methods: {
        lineItems(lineId: number) {
            if (this._perLine * lineId < this.currentList.length) {
                return this.perLine;
            }
            return this.currentList.length % lineId;
        },
        item(lineId: number, lineItemId: number) {
            return this.currentList[
                (lineId - 1) * this._perLine + lineItemId - 1
            ];
        },
    },
    components: { ListElement },
});
</script>

<style lang="scss" scoped></style>
