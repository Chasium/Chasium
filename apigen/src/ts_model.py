"""
用于生成Typescript代码
"""
from dataclasses import field
from src.models import APIData


class TsModel:
    """
    Typescript类生成类
    """

    def __init__(self, data: APIData) -> None:
        self.__apiData = data

    def class_name(self) -> str:
        """
        主类的类名
        """
        # 返回构造函数中给出的APIData的main_class的class_name
        return self.__apiData.main_class.class_name

    def get_type(self, fieldType: str, fieldNode) -> str:
        if fieldType == "bool":
            fieldType = "boolean"
        elif fieldType == "int" or fieldType == "float":
            fieldType = "number"
        elif fieldType == "list":
            fieldType = "Array"
            listType = self.get_type(
                str(type(fieldNode.element))[19: -9].lower(), fieldNode.element)
            fieldType += "<" + listType + ">"
        return fieldType

    def content(self) -> str:
        """
        生成的Typescript文件的内容
        """
        tsContent = ""

        main_class = self.__apiData.main_class
        tsContent += ("/**\n * " + main_class.description + "\n */\n")
        tsContent += "export default interface " + \
            main_class.class_name + " {\n"
        fields = main_class.fields
        for key2 in fields:
            tsContent += ("\t/**\n\t * " +
                          fields[key2].description + "\n\t */\n")
            tsContent += ("\t" + key2 + ": ")
            fieldType = self.get_type(str(type(fields[key2]))[
                                      19: -7].lower(), fields[key2])
            tsContent += (fieldType + ";\n")
        tsContent += "}\n"

        classes = self.__apiData.classes
        for key in classes:
            tsContent += ("/**\n * " + classes[key].description + "\n */\n")
            tsContent += "interface " + classes[key].class_name + " {\n"
            fields = classes[key].fields
            for key2 in fields:
                tsContent += ("\t/**\n\t * " +
                              fields[key2].description + "\n\t */\n")
                tsContent += ("\t" + key2 + ": ")
                fieldType = self.get_type(str(type(fields[key2]))[
                    19: -7].lower(), fields[key2])
                tsContent += (fieldType + ";\n")
            tsContent += "}\n"
        return tsContent
        # TODO: 返回由构造函数中给出的APIData生成的Typescript文件的全部内容
        # APIData中，classes里的每个类对应一个interface
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
        # 对应的APIData应该被转化为如下Typescript代码：
        #
        # /**
        #  * xxx
        #  */
        # interface A {
        #     /**
        #      * yyy
        #      */
        #     a: number;
        #     ...
        # }
        #
        # interface B {
        #     ...
        # }
        #
        # 另外，main_class需要根据以上规则转化为export default interface
