from flask import Request


class Test:
	"""
	测试用类1
	"""
	a1: int  # 一个int
	a2: list  # 一个list
	def __init__(self, request: Request):
		self.a1 = request.json["a1"]
		self.a2 = request.json["a2"]

class Test1:
	"""
	测试用类1临时类1
	"""
	aAbBcCDDe: bool  # 一个bool
	b: int  # 一个int
	c: list  # 一个list
	def __init__(self, request: Request):
		self.aAbBcCDDe = request.json["aAbBcCDDe"]
		self.b = request.json["b"]
		self.c = request.json["c"]

class Test2:
	"""
	测试用类2临时类1
	"""
	d: str  # 一个string
	def __init__(self, request: Request):
		self.d = request.json["d"]

