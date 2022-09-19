"""
用于生成Python代码
"""
from src.models import APIData


class PyModel:
    """
    Python类生成类
    """

    def __init__(self, data: APIData) -> None:
        # TODO: 初始化（完成后或不需要完成的情况下删除该TODO）
        pass

    def class_name(self) -> str:
        """
        主类的类名
        """
        # TODO: 返回构造函数中给出的APIData的main_class的class_name

    def content(self) -> str:
        """
        生成的Python文件的内容
        """
        # TODO: 返回由构造函数中给出的APIData生成的Python文件的全部内容
        # APIData中，classes里的每个类对应一个Python类
        # 举例：以下xml文档
        #
        # <classes>
        #     <class class-name="A">
        #         <description>xxx</description>
        #         <int>
        #             <key>a</key>
        #             <description>yyy</description>
        #         </int>
        #         ...
        #     </class>
        #     <class class-name="B">...</class>
        # </classes>
        #
        # 对应的APIData应该被转化为如下Python代码：
        #
        # from flask import Request
        #
        #
        # class A:
        #     """
        #     xxx
        #     """
        #     a: int  # yyy
        #     ...
        #     def __init__(self, request: Request):
        #         self.a = request.json["a"]
        #         ...
        #
        #
        # class B:
        #     ...
        #
        # 另外，main_class也需要根据以上规则转化成一个类
