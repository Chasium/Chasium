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
