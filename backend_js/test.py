# test client.py
# 一些比较怪的js语句
from client import getParsedScript

LONG_INPUT = """
var x = "", i = 0;
while (i<5){
	x=x + "该数字为 " + i + "<br>";
	i++
}
x;
"""
WRONG_INPUT = "hahaha"
CORRECT_INPUT = "new Date().getYear();"
NO_RET_INPUT = "console.log(\"haha\")"

def test():
    ret, code = getParsedScript(LONG_INPUT)
    print("get msg: ", ret, " type: ", type(ret))
    ret, code = getParsedScript(WRONG_INPUT)
    assert code == 1
    print("Error: ", ret, " type: ", type(ret))
    ret, code = getParsedScript(CORRECT_INPUT)
    print("get msg: ", ret, " type: ", type(ret))
    ret, code = getParsedScript(NO_RET_INPUT)
    assert code == 2
    print("No return value!", ret)

test()