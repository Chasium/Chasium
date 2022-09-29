"""
用于生成Typescript代码
"""

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

    def __get_type(self, field_type: str, field_node) -> str:
        """
        将xml文件中的类型转化为typescript语言中的类型
        """
        if field_type == "bool":
            field_type = "boolean"
        elif field_type == "int" or field_type == "float":
            field_type = "number"
        elif field_type == "list":
            field_type = "Array"
            list_type = self.__get_type(
                str(type(field_node.element))[19: -9].lower(), field_node.element)
            field_type += "<" + list_type + ">"
        return field_type

    def content(self) -> str:
        """
        生成的Typescript文件的内容
        """
        # 先将main_class转化为export default interface
        main_class = self.__apiData.main_class
        ts_content = f"/**\n * {main_class.description}\n */\n"  # 注释部分
        fields = main_class.fields
        interface_content = ""  # interface xxx{} 大括号里面的内容
        for key2 in fields:
            field_type = self.__get_type(str(type(fields[key2]))[
                19: -7].lower(), fields[key2])   # 获得变量类型
            # 注释部分
            interface_content += f"\t/**\n\t * {fields[key2].description}\n\t */\n"
            interface_content += f"\t{key2}: {field_type};\n"  # 变量声明部分
        ts_content += f"export default interface {main_class.class_name} {{\n{interface_content}}}\n\n"

        # 再将剩下的classes转化为interface
        classes = self.__apiData.classes
        for key in classes:
            ts_content += ("/**\n * " + classes[key].description + "\n */\n")
            fields = classes[key].fields
            interface_content = ""  # interface Test{ } 大括号里面的内容
            for key2 in fields:
                field_type = self.__get_type(str(type(fields[key2]))[
                    19: -7].lower(), fields[key2])   # 获得变量类型
                # 注释部分
                interface_content += f"\t/**\n\t * {fields[key2].description}\n\t */\n"
                interface_content += f"\t{key2}: {field_type};\n"  # 变量声明部分
            ts_content += f"interface {classes[key].class_name} {{\n{interface_content}}}\n\n"

        return ts_content
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
