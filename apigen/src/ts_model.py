"""
用于生成Typescript代码
"""

from src.models import APIData  # pylint: disable=import-error

# 这里存放 const string

CLASS_DESCRIPTION = '''/**
 * {description}
 */
'''
VARIABLE_DECLARATION = '''
    /**
     * {description}
     */
    {key}: {field_type};
'''


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
            field_type += ("<" + list_type + ">")
        return field_type

    def content(self) -> str:
        """
        生成的Typescript文件的内容
        """
        # 先将main_class转化为export default interface
        main_class = self.__apiData.main_class
        ts_content = CLASS_DESCRIPTION.format(
            description=main_class.description)
        fields = main_class.fields
        interface_content = ""  # interface xxx{} 大括号里面的内容
        for key2 in fields:
            field_type = self.__get_type(str(type(fields[key2]))[
                19: -7].lower(), fields[key2])   # 获得变量类型
            interface_content += VARIABLE_DECLARATION.format(
                description=fields[key2].description, key=key2, field_type=field_type)

        ts_content += \
            f"export default interface {main_class.class_name} {{{interface_content}}}\n\n"

        # 再将剩下的classes转化为interface
        classes = self.__apiData.classes
        for key in classes:
            ts_content += CLASS_DESCRIPTION.format(
                description=classes[key].description)

            fields = classes[key].fields
            interface_content = ""  # interface Test{ } 大括号里面的内容
            for key2 in fields:
                field_type = self.__get_type(str(type(fields[key2]))[
                    19: -7].lower(), fields[key2])   # 获得变量类型
                interface_content += VARIABLE_DECLARATION.format(
                    description=fields[key2].description, key=key2, field_type=field_type)
            ts_content += f"interface {classes[key].class_name} {{{interface_content}}}\n\n"

        return ts_content
