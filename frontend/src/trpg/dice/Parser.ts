import type Tokenizer from './Tokenizer';
import { TokenType, type OpToken, type Token } from './Tokens';
import { BiOpNode, MonoOpNode, NumNode, type TreeNode } from './TreeNode';

const PRIORITIES: Map<
    | TokenType.ADD
    | TokenType.SUB
    | TokenType.MUL
    | TokenType.DIV
    | TokenType.DIC,
    number
> = new Map();
PRIORITIES.set(TokenType.ADD, 0);
PRIORITIES.set(TokenType.SUB, 0);
PRIORITIES.set(TokenType.MUL, 1);
PRIORITIES.set(TokenType.DIV, 1);
PRIORITIES.set(TokenType.DIC, 2);

/**
 * 解析器
 */
export default class Parser {
    readonly root: TreeNode;
    /**
     * 使用优先级爬坡算法把Tokenizer解析为运算符树
     * @param tokens 要解析的Tokenizer
     */
    constructor(tokens: Tokenizer) {
        this.root = this.parseFrom(tokens, false);
    }

    private parseFrom(tokens: Tokenizer, inBracket: boolean): TreeNode {
        const numStack: TreeNode[] = [];
        const opStack: OpToken[] = [];
        for (;;) {
            if (tokens.empty) {
                if (inBracket) {
                    let tempNode = this.popStacks(numStack, opStack);
                    while ((tempNode as any).rChild != null) {
                        tempNode = (tempNode as any).rChild;
                    }
                    throw Error(
                        `Missing ')' at position ${tempNode.token.index + 2}`
                    );
                } else {
                    return this.popStacks(numStack, opStack);
                }
            }
            const token = tokens.nextToken();
            if (token.type == TokenType.NUM) {
                numStack.push(new NumNode(token));
            } else if (token.type == TokenType.LBR) {
                numStack.push(this.parseFrom(tokens, true));
            } else if (token.type == TokenType.RBR) {
                if (inBracket) {
                    return this.popStacks(numStack, opStack);
                } else {
                    throw Error(`Illegal ')' at position ${token.index + 1}`);
                }
            } else if (token.type == TokenType.NEG) {
                numStack.push(
                    new MonoOpNode(token, this.parseInNeg(token, tokens))
                );
            }
        }
    }

    private popStacks(numStack: TreeNode[], opStack: OpToken[]): TreeNode {
        for (;;) {
            if (opStack.length == 0) {
                return numStack[0];
            } else {
                const rNum = numStack.pop();
                const lNum = numStack.pop();
                const op = opStack.pop();
                if (rNum == null || lNum == null || op == null) {
                    throw Error('Unknown error');
                }
                numStack.push(new BiOpNode(op, lNum, rNum));
            }
        }
    }

    private parseInNeg(outerNeg: Token, tokens: Tokenizer): TreeNode {
        if (tokens.empty) {
            throw Error(
                `Missing number or expression at position ${outerNeg.index + 2}`
            );
        } else {
            const token = tokens.nextToken();
            if (token.type == TokenType.NEG) {
                return new MonoOpNode(token, this.parseInNeg(token, tokens));
            } else if (token.type == TokenType.NUM) {
                return new NumNode(token);
            } else if (token.type == TokenType.LBR) {
                return this.parseFrom(tokens, true);
            } else {
                throw Error('Unknown error');
            }
        }
    }
}
