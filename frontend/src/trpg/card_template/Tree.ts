import type { Property } from './Property';
import type { Area } from './Area';
import type CardTemplate from './CardTemplate';
import type { Column } from './Column';
import type { Row } from './Row';

export enum NodeType {
    CARD,
    COLUMN,
    AREA,
    ROW,
    PROPERTY,
}

interface IBaseNode {
    id: number;
    type: NodeType;
    label: string;
    children: Tree[];
    parent?: Tree;
}

export interface ICardNode extends IBaseNode {
    type: NodeType.CARD;
    card: CardTemplate;
    children: IColumnNode[];
    parent: undefined;
}

export interface IColumnNode extends IBaseNode {
    type: NodeType.COLUMN;
    column: Column;
    children: IAreaNode[];
    parent: ICardNode;
}

export interface IAreaNode extends IBaseNode {
    type: NodeType.AREA;
    area: Area;
    children: IRowNode[];
    parent: IColumnNode;
}

export interface IRowNode extends IBaseNode {
    type: NodeType.ROW;
    row: Row;
    children: IPropertyNode[];
    parent: IAreaNode;
}

export interface IPropertyNode extends IBaseNode {
    type: NodeType.PROPERTY;
    property: Property;
    children: [];
    parent: IRowNode;
}

export type Tree =
    | ICardNode
    | IColumnNode
    | IAreaNode
    | IRowNode
    | IPropertyNode;
