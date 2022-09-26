import type { Row } from './Row';

export default class CardTemplate {
    rows: Row[] = [];
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
