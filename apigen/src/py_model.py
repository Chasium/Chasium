"""
用于生成Python代码
"""
from src.models import APIData, ListField, ObjectField


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

    def content(self) -> str:
        """
        生成的Python文件的内容
        """
        # TODO: 使用f-string代替字符串加法来构造代码，提高可读性
        # TODO: 使用isinstance代替type字符串，提高可读性和效率
        # TODO: 使用多行字符串代替字符串内的\n，提高可读性
        # TODO: 使用四个空格代替\t
        pythonContent = "from flask import Request\n\n\n"
        classes = self.__apiData.classes

        main_class = self.__apiData.main_class
        pythonContent += ("class " + main_class.class_name + ":\n")
        pythonContent += ("\t\"\"\"\n\t" +
                          main_class.description + "\n\t\"\"\"\n")
        fields = main_class.fields
        for key2 in fields:
            fieldType = str(type(fields[key2]))[19: -7].lower()
            if fieldType == 'string':
                fieldType = 'str'
            pythonContent += ("\t" + key2 + ': ' +
                              fieldType + "  # " + fields[key2].description + "\n")
            # type(fields[key2]))形如 <class src.models.BoolField>
        pythonContent += "\tdef __init__(self, request: Request):\n"
        for key2 in fields:
            pythonContent += ("\t\tself." + key2 +
                              " = request.json[\"" + key2 + "\"]\n")
        pythonContent += "\n"

        for key in classes:
            pythonContent += ("class " + classes[key].class_name + ":\n")
            pythonContent += ("\t\"\"\"\n\t" +
                              classes[key].description + "\n\t\"\"\"\n")
            fields = classes[key].fields
            for key2 in fields:
                fieldType = str(type(fields[key2]))[19: -7].lower()
                if fieldType == 'string':
                    fieldType = 'str'
                pythonContent += ("\t" + key2 + ': ' +
                                  fieldType + "  # " + fields[key2].description + "\n")
                # type(fields[key2]))形如 <class src.models.BoolField>
            pythonContent += "\tdef __init__(self, request: Request):\n"
            for key2 in fields:
                if isinstance(fields[key2], ObjectField):
                    obj_field: ObjectField = fields[key2]
                    # 以下是一个使用f-string的示例
                    pythonContent += f'\t\tself.{key2} = {obj_field.obj_class.class_name}(request.json["{key2}"])\n'
                elif isinstance(fields[key2], ListField):
                    # TODO: 完成对数组类型的初始化（注意递归多层数组）
                    pass
                else:
                    pythonContent += ("\t\tself." + key2 +
                                      " = request.json[\"" + key2 + "\"]\n")
            pythonContent += "\n"
        return pythonContent
