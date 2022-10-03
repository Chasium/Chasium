export default class EvalScript {
    private obj: any;
    constructor(script: string) {
        this.obj = eval(script);
    }
    run() {
        if (
            typeof this.obj == 'number' ||
            typeof this.obj == 'boolean' ||
            typeof this.obj == 'string'
        ) {
            return this.obj;
        } else if (typeof this.obj == 'function') {
            return this.obj();
        }
    }
}
