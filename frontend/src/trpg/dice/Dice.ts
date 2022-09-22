import Parser from './Parser';
import Tokenizer from './Tokenizer';
import type { TreeNode } from './TreeNode';

/**
 * TRPG所用的复合多面骰子
 *
 * 复合多面骰子是TRPG描述骰子使用的术语,由数字以及运算符'+'，'-'，'\*'，'/'，'d'组成。
 * 其中，'+'，'-'，'\*'，'/'的意义与一般编程语言一致。（注意，'/'为整除而不是浮点数除法）
 * 'd'是一个特殊运算符，"ndm"表示“生成n个范围为闭区间[1,m]的随机整数，并把它们累加”。
 * 注意，在复合多面骰子中，表达式中所有数以及运算结果均为整数。
 */
export default class Dice {
    private root: TreeNode;

    /**
     * 构造一个符合多面骰子
     * @param origin 用于描述它的表达式
     */
    constructor(readonly origin: string) {
        this.root = new Parser(new Tokenizer(origin)).root;
    }
    value() {
        return this.root.value();
    }
}
