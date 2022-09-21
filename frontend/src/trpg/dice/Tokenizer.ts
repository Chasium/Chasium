import { TokenType, type Token } from './Tokens';

/**
 * Token解析器
 *
 * 通过将表达式传入构造函数来构造一个Token解析器。
 * 其本身相当于一个Token的队列，可以调用nextToken获得队列中下一个Token，或使用empty属性判断其是否为空
 */
export default class Tokenizer {
    private tokens: Token[] = [];
    private currentIndex = 0;
    /**
     * 通过有限状态自动机来解析表达式
     * @param expression 要解析的表达式
     * @throws 表达式出现非法字符时抛出Error
     */
    constructor(expression: string) {
        enum State {
            INIT,
            READING_NUM,
            READ_NUM,
        }

        let currentState = State.INIT;
        let readingNumOffset = 0;
        let readingNum = '';

        for (let i = 0; i < expression.length; i++) {
            const char = expression[i];
            if (currentState == State.INIT) {
                if (/[0-9]/.test(char)) {
                    currentState = State.READING_NUM;
                    readingNum += char;
                    readingNumOffset = i;
                } else if (/-/.test(char)) {
                    currentState = State.INIT;
                    this.tokens.push({ type: TokenType.NEG, index: i });
                } else if (/\(/.test(char)) {
                    currentState = State.INIT;
                    this.tokens.push({ type: TokenType.LBR, index: i });
                } else if (/\s/.test(char)) {
                    continue;
                } else {
                    throw Error(`Illegal '${char}' at position ${i + 1}`);
                }
            } else if (currentState == State.READING_NUM) {
                if (/[0-9]/.test(char)) {
                    readingNum += char;
                } else {
                    if (readingNum.length > 1 && readingNum[0] == '0') {
                        throw Error(
                            `Illegal number '${readingNum}' at position ${
                                readingNumOffset + 1
                            }: a number cannot start with 0`
                        );
                    }
                    this.tokens.push({
                        type: TokenType.NUM,
                        value: parseInt(readingNum),
                        index: readingNumOffset,
                    });
                    readingNum = '';
                    if (/\+/.test(char)) {
                        this.tokens.push({ type: TokenType.ADD, index: i });
                        currentState = State.INIT;
                    } else if (/-/.test(char)) {
                        this.tokens.push({ type: TokenType.SUB, index: i });
                        currentState = State.INIT;
                    } else if (/\*/.test(char)) {
                        this.tokens.push({ type: TokenType.MUL, index: i });
                        currentState = State.INIT;
                    } else if (/\//.test(char)) {
                        this.tokens.push({ type: TokenType.DIV, index: i });
                        currentState = State.INIT;
                    } else if (/d/.test(char)) {
                        this.tokens.push({ type: TokenType.DIC, index: i });
                        currentState = State.INIT;
                    } else if (/\)/.test(char)) {
                        this.tokens.push({ type: TokenType.RBR, index: i });
                        currentState = State.READ_NUM;
                    } else if (/\s/.test(char)) {
                        currentState = State.READ_NUM;
                    } else {
                        throw Error(`Illegal '${char}' at position ${i + 1}`);
                    }
                }
            } else if (currentState == State.READ_NUM) {
                if (/\+/.test(char)) {
                    this.tokens.push({ type: TokenType.ADD, index: i });
                    currentState = State.INIT;
                } else if (/-/.test(char)) {
                    this.tokens.push({ type: TokenType.SUB, index: i });
                    currentState = State.INIT;
                } else if (/\*/.test(char)) {
                    this.tokens.push({ type: TokenType.MUL, index: i });
                    currentState = State.INIT;
                } else if (/\//.test(char)) {
                    this.tokens.push({ type: TokenType.DIV, index: i });
                    currentState = State.INIT;
                } else if (/d/.test(char)) {
                    this.tokens.push({ type: TokenType.DIC, index: i });
                    currentState = State.INIT;
                } else if (/\)/.test(char)) {
                    this.tokens.push({ type: TokenType.RBR, index: i });
                    currentState = State.READ_NUM;
                } else if (/\s/.test(char)) {
                    currentState = State.READ_NUM;
                } else {
                    throw Error(`Illegal '${char}' at position ${i + 1}`);
                }
            }
        }

        if (currentState == State.READING_NUM) {
            if (readingNum.length > 1 && readingNum[0] == '0') {
                throw Error(
                    `Illegal number '${readingNum}' at position ${
                        readingNumOffset + 1
                    }: a number cannot start with 0`
                );
            }
            this.tokens.push({
                type: TokenType.NUM,
                value: parseInt(readingNum),
                index: readingNumOffset,
            });
        }
    }

    nextToken() {
        if (this.currentIndex >= this.tokens.length) {
            throw Error(`Tokenizer ${this} is empty`);
        }
        const out = this.tokens[this.currentIndex];
        this.currentIndex++;
        if (this.currentIndex >= this.tokens.length) {
            this.tokens = [];
        }
        return out;
    }

    get empty() {
        return this.currentIndex >= this.tokens.length;
    }
}
