import type { Property } from './Property';

export class Row {
    properties: Property[] = [];

    constructor(
        public id: number,
        public nameScript: string,
        public needCheck: boolean,
        public checkScript: string
    ) {}
}
