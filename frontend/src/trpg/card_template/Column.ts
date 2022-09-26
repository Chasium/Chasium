import type { Area } from './Area';

export class Column {
    areas: Area[] = [];
    constructor(
        public id: number,
        public needCheck: boolean,
        public checkScript: string
    ) {}
}
