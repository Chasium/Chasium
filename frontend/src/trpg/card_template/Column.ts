import type { Area } from './Area';

export class Column {
    areas: Area[] = [];
    constructor(
        public id: number,
        public nameScript: string,
        public needCheck: boolean,
        public checkScript: string
    ) {}
}
