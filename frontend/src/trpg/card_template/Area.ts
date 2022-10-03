import type { Row } from './Row';

export enum AreaType {
    PERMANENT,
    IN_GAME,
}

export class Area {
    rows: Row[] = [];
    constructor(
        public id: number,
        public nameScript: string,
        public type: AreaType,
        public needCheck: boolean,
        public checkScript: string,
        public needManualCheck: boolean
    ) {}
}
