"""
用于生成Typescript代码
"""
from src.models import APIData


class TsModel:
    """
    Typescript类生成类
    """

    def __init__(self, data: APIData) -> None:
        # TODO: 初始化（完成后或不需要完成的情况下删除该TODO）
        pass

    def content(self) -> str:
        """
        生成的Typescript文件的内容
        """
        # TODO: 返回由构造函数中给出的APIData生成的Typescript文件的全部内容
        # APIData中，classes里的每个类对应一个interface
        # 举例：以下xml文档
        # <classes>
        #     <class class-name="A">
        #         <int>
        #             <key>a</key>
        #             <description>xxx</description>
        #         </int>
        #         ...
        #     </class>
        #     <class class-name="B">...</class>
        # </classes>
        # 对应的APIData应该被转化为如下Typescript代码：
        # interface A {
        #     /**
        #      * xxx
        #      */
        #     a: int;
        #     ...
        # }
        #
        # interface B {
        #     ...
        # }
        # 另外，main_class需要根据以上规则转化为export default interface
