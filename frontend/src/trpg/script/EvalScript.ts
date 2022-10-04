export default class EvalScript {
    private obj: any;
    constructor(script: string) {
        if (!this.check(script)) {
            throw Error('Maybe malicious code!');
        }
        this.obj = eval(script);
    }
    check(script: string): boolean {
        //TODO: 检查是否可能为恶意代码
        /**
         * 使用espree解析传入的js字符串，并按照以下规则判断代码合法性：
         *
         * 代码必须是一个运算结果为number/string/boolean类型的表达式，
         * 或者一个返回上述类型的函数。
         *
         * 如果代码是表达式，其中只能使用基本的加减乘除等运算符以及白名单中允许的全局函数，
         * 不能使用其他全局变量和函数。
         *
         * 如果代码是函数，代码中允许的操作：
         * * 创建并使用局部变量和函数（局部函数内允许和不允许的操作与主函数相同）
         * * 使用函数参数
         * * 使用白名单中允许的全局函数
         * * 书写如上文所述的表达式
         * * 使用条件判断和循环
         * 代码中绝对不允许的操作：
         * * 调用白名单之外的全局变量和函数
         * * 进行网络通信或引入外部库
         * * 修改白名单中全局函数的实现
         * * 修改js内置对象的原型
         *
         * 白名单：
         * * parseInt
         * * parseFloat
         * * toString
         */
        return true;
    }
    run(...args: any) {
        if (
            typeof this.obj == 'number' ||
            typeof this.obj == 'boolean' ||
            typeof this.obj == 'string'
        ) {
            return this.obj;
        } else if (typeof this.obj == 'function') {
            return this.obj(args);
        }
    }
}
