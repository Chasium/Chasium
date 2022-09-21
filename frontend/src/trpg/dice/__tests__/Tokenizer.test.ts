import { describe, it, expect } from 'vitest';
import Tokenizer from '../Tokenizer';
import { TokenType } from '../Tokens';

describe('测试Tokenizer', () => {
    it('从有效表达式构造', () => {
        const testTokenizer = new Tokenizer('1-2+-3*(5d(67/8))');
        expect(testTokenizer.nextToken().type).toBe(TokenType.NUM);
        expect(testTokenizer.nextToken().type).toBe(TokenType.SUB);
        expect(testTokenizer.nextToken().type).toBe(TokenType.NUM);
        expect(testTokenizer.nextToken().type).toBe(TokenType.ADD);
        expect(testTokenizer.nextToken().type).toBe(TokenType.NEG);
        expect(testTokenizer.nextToken().type).toBe(TokenType.NUM);
        expect(testTokenizer.nextToken().type).toBe(TokenType.MUL);
        expect(testTokenizer.nextToken().type).toBe(TokenType.LBR);
        expect(testTokenizer.nextToken().type).toBe(TokenType.NUM);
        expect(testTokenizer.nextToken().type).toBe(TokenType.DIC);
        expect(testTokenizer.nextToken().type).toBe(TokenType.LBR);
        expect(testTokenizer.nextToken().type).toBe(TokenType.NUM);
        expect(testTokenizer.nextToken().type).toBe(TokenType.DIV);
        expect(testTokenizer.nextToken().type).toBe(TokenType.NUM);
        expect(testTokenizer.nextToken().type).toBe(TokenType.RBR);
        expect(testTokenizer.nextToken().type).toBe(TokenType.RBR);
        expect(testTokenizer.empty).toBe(true);
    });
    it('从错误表达式构造', () => {
        try {
            new Tokenizer('+2');
        } catch (e) {
            console.log(e);
        }
        try {
            new Tokenizer('1 1');
        } catch (e) {
            console.log(e);
        }
    });
});
