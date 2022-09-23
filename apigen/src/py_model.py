"""
用于生成Python代码
"""
from src.models import APIData


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
                pythonContent += ("\t\tself." + key2 +
                                  " = request.json[\"" + key2 + "\"]\n")
            pythonContent += "\n"
        return pythonContent
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
