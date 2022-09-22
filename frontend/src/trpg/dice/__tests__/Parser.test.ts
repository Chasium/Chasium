import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import Parser from '../Parser';
import Tokenizer from '../Tokenizer';

describe('测试Parser', () => {
    let originalRandom: any = null;
    beforeEach(() => {
        originalRandom = Math.random;
        Math.random = vi.fn(() => 0.501);
    });
    afterEach(() => {
        Math.random = originalRandom;
    });
    it('从正确表达式构建', () => {
        const testParser = new Parser(new Tokenizer('1d6'));
        expect(testParser.root.value()).toBe(4);
        const testParser2 = new Parser(new Tokenizer('9/3+2d(8-3)*5--4'));
        expect(testParser2.root.value()).toBe(37);
    });
    it('从错误表达式构造', () => {
        try {
            new Parser(new Tokenizer('(1+1))'));
        } catch (e) {
            console.log(e);
        }
        try {
            new Parser(new Tokenizer('3+'));
        } catch (e) {
            console.log(e);
        }
    });
});
