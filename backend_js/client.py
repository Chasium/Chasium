# client.py
# 单独运行可以当成一个客户端直接输入js代码进行测试
# 其他python文件要解析js代码可以调用 getParsedScript() 函数
# 返回的result为运行结果，code代表是否出错（后面可能就不用了

import websockets
import asyncio
import json

global RESULT, CODE


async def listen(send_msg: str):
    url = "ws://127.0.0.1:1234"
    async with websockets.connect(url) as ws:
        msg = await ws.recv()
        assert msg == "hello, this is server.ts!"  # wait till connected
        # 接着发送想要给ts server端发送的数据
        await ws.send(send_msg)
        msg = await ws.recv()
        global RESULT, CODE # 因为好像搞不到返回值，所以用了全局变量
        RESULT = json.loads(msg)["result"]
        CODE = json.loads(msg)["code"]


# 这个函数可以将传入的js字符串，返回运行得到的返回值和是否运行出错
def getParsedScript(script: str):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(listen(script))
    return RESULT, CODE

# 用于测试test，可以输入js代码进行测试
if __name__ == "__main__":
    while 1:
        input_msg = input("> ")
        if input_msg == "quit" or input_msg == "exit" :
            break
        ret, code = getParsedScript(input_msg)
        if code == 0:
            print("get msg: ", ret, " type: ", type(ret))
        elif code == 1:
            print("ERROR! ", ret)
        else:
            print("No return value!")