import type { Column } from './Column';

export default class CardTemplate {
    columns: Column[] = [];
    constructor(
        public name: string,
        public description: string,
        public needCheck: boolean,
        public checkScript: string,
        public coverPropertyId: number,
        public cardDescriptionScript: string,
        public inGameCardScript: string
    ) {}
}
