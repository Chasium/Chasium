import EvalScript from "../frontend/src/trpg/script/EvalScript";

export default function EvalJSScript(script: string) {
  var ret_json = { result: "", code: 0 }; // result 是 eval 的结果或报错信息， code 代表是否出错
  try {
    var e = new EvalScript(script);
    var res = e.run();
    console.log("res: ", res);
    if (res === undefined) {
      // 如果传入的js代码没有返回值，code为2
      ret_json = { result: "", code: 2 };
    } else {
      // 正常情况，code为0
      ret_json = { result: e.run(), code: 0 };
    }
  } catch (error) {
    // 如果传入的js代码有bug，code为1
    console.log(error);
    ret_json = { result: String(error), code: 1 };
  }
  return ret_json;
}
