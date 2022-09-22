import { TokenType, type NumToken, type Token } from './Tokens';

export interface TreeNode {
    readonly token: Token;
    value(): number;
}

export class NumNode implements TreeNode {
    constructor(readonly token: NumToken) {}
    value(): number {
        return this.token.value;
    }
}

export class MonoOpNode implements TreeNode {
    constructor(readonly token: Token, readonly rChild: TreeNode) {}
    value(): number {
        return -this.rChild.value();
    }
}

export class BiOpNode implements TreeNode {
    constructor(
        readonly token: Token,
        readonly lChild: TreeNode,
        readonly rChild: TreeNode
    ) {}
    value(): number {
        if (this.token.type == TokenType.ADD) {
            return this.lChild.value() + this.rChild.value();
        } else if (this.token.type == TokenType.SUB) {
            return this.lChild.value() - this.rChild.value();
        } else if (this.token.type == TokenType.MUL) {
            return this.lChild.value() * this.rChild.value();
        } else if (this.token.type == TokenType.DIV) {
            const out = this.lChild.value() / this.rChild.value();
            return out > 0 ? Math.floor(out) : Math.ceil(out);
        } else if (this.token.type == TokenType.DIC) {
            let out = 0;
            const lValue = this.lChild.value();
            for (let i = 0; i < lValue; i++) {
                out += Math.ceil(Math.random() * this.rChild.value());
            }
            return out;
        } else {
            throw Error('Unknown error');
        }
    }
}
