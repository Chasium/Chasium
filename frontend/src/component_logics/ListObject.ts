export class BaseListObject {}

export abstract class ListObject<T = any> extends BaseListObject {
    abstract pages(): number;
    abstract get(page: number): T;
    abstract getImage(item: T): string;
    abstract getName(item: T): string;
    abstract getDescription(item: T): string;
    abstract onItemClick(item: T): void;
}
