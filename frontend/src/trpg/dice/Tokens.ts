export enum TokenType {
    /**
     * 数字
     */
    NUM,
    /**
     * 负号
     */
    NEG,
    /**
     * 加
     */
    ADD,
    /**
     * 减
     */
    SUB,
    /**
     * 乘
     */
    MUL,
    /**
     * 除
     */
    DIV,
    /**
     * d（掷骰）
     */
    DIC,
    /**
     * 左括号
     */
    LBR,
    /**
     * 右括号
     */
    RBR,
}

/**
 * 数字Token
 *
 * type只能为TokenType.NUM，具有数字值
 */
export interface NumToken {
    type: TokenType.NUM;
    index: number;
    value: number;
}

/**
 * 运算符与括号Token
 *
 * 只具有type，不具有值，且type不能为TokenType.NUM
 */
export interface OpToken {
    type:
        | TokenType.NEG
        | TokenType.ADD
        | TokenType.SUB
        | TokenType.MUL
        | TokenType.DIV
        | TokenType.DIC
        | TokenType.LBR
        | TokenType.RBR;
    index: number;
}

/**
 * 合并两类型Token，成为Token类型
 */
export type Token = NumToken | OpToken;
