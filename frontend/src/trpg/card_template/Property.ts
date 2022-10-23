/**
 * 属性类型
 */
export enum PropertyType {
    INT,
    FLOAT,
    BOOL,
    STRING,
    SELECTION,
    CALCULATED_INT,
    CALCULATED_FLOAT,
    CALCULATED_BOOL,
    CALCULATED_STRING,
    IMAGE,
    BUTTON,
}

export interface IProperty {
    type: PropertyType;
    id: number;
    nameScript: string;
}

export interface IBasicProperty extends IProperty {
    type:
        | PropertyType.INT
        | PropertyType.FLOAT
        | PropertyType.BOOL
        | PropertyType.STRING;
    needCheck: boolean;
    checkScript: string;
}

export interface IIntProperty extends IBasicProperty {
    type: PropertyType.INT;
}

export interface IFloatProperty extends IBasicProperty {
    type: PropertyType.FLOAT;
    precisionScript: string;
}

export interface IBoolProperty extends IBasicProperty {
    type: PropertyType.BOOL;
}

export interface IStringProperty extends IBasicProperty {
    type: PropertyType.STRING;
}

export interface ISelectionProperty extends IProperty {
    type: PropertyType.SELECTION;
    valueClassScript: string;
    needCheck: boolean;
    checkScript: string;
}

export interface ICalculatedProperty extends IProperty {
    type:
        | PropertyType.CALCULATED_INT
        | PropertyType.CALCULATED_FLOAT
        | PropertyType.CALCULATED_BOOL
        | PropertyType.CALCULATED_STRING;
    calculateScript: string;
    needCheck: boolean;
    checkScript: string;
}

export interface ICalculatedIntProperty extends ICalculatedProperty {
    type: PropertyType.CALCULATED_INT;
}

export interface ICalculatedFloatProperty extends ICalculatedProperty {
    type: PropertyType.CALCULATED_FLOAT;
    precisionScript: string;
}

export interface ICalculatedBoolProperty extends ICalculatedProperty {
    type: PropertyType.CALCULATED_BOOL;
}

export interface ICalculatedStringProperty extends ICalculatedProperty {
    type: PropertyType.CALCULATED_STRING;
}

export interface IImageProperty extends IProperty {
    type: PropertyType.IMAGE;
}

export enum ButtonPropertyPhase {
    ANY,
    IN_CREATION,
    IN_GAME,
}

export interface IButtonProperty extends IProperty {
    type: PropertyType.BUTTON;
    phase: ButtonPropertyPhase;
    textScript: string;
    clickScript: string;
}

export type Property =
    | IIntProperty
    | IFloatProperty
    | IBoolProperty
    | IStringProperty
    | ISelectionProperty
    | ICalculatedIntProperty
    | ICalculatedFloatProperty
    | ICalculatedBoolProperty
    | ICalculatedStringProperty
    | IImageProperty
    | IButtonProperty;

export class IntProperty implements IIntProperty {
    type: PropertyType.INT = PropertyType.INT;

    constructor(
        public id: number,
        public nameScript: string,
        public needCheck: boolean,
        public checkScript: string
    ) {}
}

export class FloatProperty implements IFloatProperty {
    type: PropertyType.FLOAT = PropertyType.FLOAT;

    constructor(
        public id: number,
        public nameScript: string,
        public precisionScript: string,
        public needCheck: boolean,
        public checkScript: string
    ) {}
}

export class BoolProperty implements IBoolProperty {
    type: PropertyType.BOOL = PropertyType.BOOL;

    constructor(
        public id: number,
        public nameScript: string,
        public needCheck: boolean,
        public checkScript: string
    ) {}
}

export class StringProperty implements IStringProperty {
    type: PropertyType.STRING = PropertyType.STRING;

    constructor(
        public id: number,
        public nameScript: string,
        public needCheck: boolean,
        public checkScript: string
    ) {}
}

export class SelectionProperty implements ISelectionProperty {
    type: PropertyType.SELECTION = PropertyType.SELECTION;
    constructor(
        public id: number,
        public nameScript: string,
        public valueClassScript: string,
        public needCheck: boolean,
        public checkScript: string
    ) {}
}

export class CalculatedIntProperty implements ICalculatedIntProperty {
    type: PropertyType.CALCULATED_INT = PropertyType.CALCULATED_INT;

    constructor(
        public id: number,
        public nameScript: string,
        public calculateScript: string,
        public needCheck: boolean,
        public checkScript: string
    ) {}
}

export class CalculatedFloatProperty implements ICalculatedFloatProperty {
    type: PropertyType.CALCULATED_FLOAT = PropertyType.CALCULATED_FLOAT;

    constructor(
        public id: number,
        public nameScript: string,
        public calculateScript: string,
        public precisionScript: string,
        public needCheck: boolean,
        public checkScript: string
    ) {}
}

export class CalculatedBoolProperty implements ICalculatedBoolProperty {
    type: PropertyType.CALCULATED_BOOL = PropertyType.CALCULATED_BOOL;

    constructor(
        public id: number,
        public nameScript: string,
        public calculateScript: string,
        public needCheck: boolean,
        public checkScript: string
    ) {}
}

export class CalculatedStringProperty implements ICalculatedStringProperty {
    type: PropertyType.CALCULATED_STRING = PropertyType.CALCULATED_STRING;

    constructor(
        public id: number,
        public nameScript: string,
        public calculateScript: string,
        public needCheck: boolean,
        public checkScript: string
    ) {}
}

export class ImageProperty implements IImageProperty {
    type: PropertyType.IMAGE = PropertyType.IMAGE;
    constructor(public id: number, public nameScript: string) {}
}

export class ButtonProperty implements IButtonProperty {
    type: PropertyType.BUTTON = PropertyType.BUTTON;
    constructor(
        public id: number,
        public nameScript: string,
        public phase: ButtonPropertyPhase,
        public textScript: string,
        public clickScript: string
    ) {}
}
