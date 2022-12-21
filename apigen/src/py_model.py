"""
用于生成Python代码
"""
from src.models import APIData  # pylint:disable=import-error

CLASS_DECLARATION = '''
class {name}:
    \"\"\"
    {description}
    \"\"\"
'''
VARIABLE_DECLARATION = "    {key}: {type}  # {description}\n"
CLASS_INIT = "    def __init__(self, request: Request):\n"
INIT_CONTENT = "        self.{key} = request.json[\"{key}\"]\n"


class PyModel:
    """
    Python类生成类
    """

    def __init__(self, data: APIData) -> None:
        self.__apiData = data

    def class_name(self) -> str:
        """
        主类的类名
        """
        # 返回构造函数中给出的APIData的main_class的class_name
        return self.__apiData.main_class.class_name

    def __get_type(self, field: str) -> str:
        """
        将xml文件中的类型转化为python语言中的类型
        """
        field_type = field[19: -7].lower()
        if field_type == 'string':
            field_type = 'str'
        return field_type

    def content(self) -> str:
        """
        生成的Python文件的内容
        """
        python_content = "from flask import Request\n\n"

        # 先将main_class转化为class xxx:
        main_class = self.__apiData.main_class
        python_content += CLASS_DECLARATION.format(
            name=main_class.class_name, description=main_class.description)
        fields = main_class.fields
        for key2 in fields:
            field_type = self.__get_type(str(type(fields[key2])))  # 获得变量类型
            python_content += VARIABLE_DECLARATION.format(
                key=key2, type=field_type, description=fields[key2].description)
        python_content += CLASS_INIT
        for key2 in fields:
            python_content += INIT_CONTENT.format(key=key2)

        # 再处理其余的classes
        classes = self.__apiData.classes
        for key in classes:
            python_content += CLASS_DECLARATION.format(
                name=classes[key].class_name, description=classes[key].description)
            fields = classes[key].fields
            for key2 in fields:
                field_type = self.__get_type(str(type(fields[key2])))  # 获得变量类型
                python_content += VARIABLE_DECLARATION.format(
                    key=key2, type=field_type, description=fields[key2].description)
            python_content += CLASS_INIT
            for key2 in fields:
                python_content += INIT_CONTENT.format(key=key2)

        return python_content
