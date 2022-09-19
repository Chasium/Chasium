"""
和xml中各元素对应的各类
"""
import re
from typing import Any, Dict, List, Tuple


KEY = re.compile(r'^[a-z]+[0-9]*([A-Z][a-z]*[0-9]*)*$')
CLASS_NAME = re.compile(r'^([A-Z][a-z]*[0-9]*)+$')
API_PATH = re.compile(
    r'^((([a-z]+[0-9]*-)*[a-z]+[0-9]*)/)*(([a-z]+[0-9]*-)*[a-z]+[0-9]*)$'
)


class Field:
    """
    IntField，FloatField等的基类
    """
    key: str
    description: str

    def __init__(self, xml: Any) -> None:
        children = xml.childNodes()
        if children is None or len(children) < 2:
            raise Exception('Illegal field node')
        self.key = children[0].firstChild.data
        self.description = children[1].firstChild.data
        if not isinstance(self.key, str):
            raise Exception('Illegal key')
        if not KEY.match(self.key):
            raise Exception('Illegal key format')
        if not isinstance(self.description, str):
            raise Exception('Illegal description')


class IntField(Field):
    """
    对应xml中<int>
    """


class FloatField(Field):
    """
    对应xml中<float>
    """


class BoolField(Field):
    """
    对应xml中<bool>
    """


class StringField(Field):
    """
    对应xml中<string>
    """


class Element:
    """
    IntElement，FloatElement等的基类
    """
    description: str

    def __init__(self, xml: Any) -> None:
        children = xml.childNodes()
        if children is None or len(children) < 1:
            raise Exception('Illegal element node')
        self.description = children[0].firstChild.data
        if not isinstance(self.description, str):
            raise Exception('Illegal description')


class IntElement(Element):
    """
    对应xml中<int-element>
    """


class FloatElement(Element):
    """
    对应xml中<float-element>
    """


class BoolElement(Element):
    """
    对应xml中<bool-element>
    """


class StringElement(Element):
    """
    对应xml中<string-element>
    """


class Class:
    """
    对应xml中<class>
    """
    class_name: str
    description: str
    fields: Dict[str, Field]

    def __init__(self, xml: Any, objs: List[Tuple[str, Any]]) -> None:
        self.class_name = xml.getAttribute('class-name')
        if not isinstance(self.class_name, str):
            raise Exception(f'Illegal class name: {self.class_name}')
        if not CLASS_NAME.match(self.class_name):
            raise Exception(f'Illegal class name format: {self.class_name}')

        children = xml.childNodes()
        if children is None or len(children) < 2:
            raise Exception('Illegal class')
        self.description = children[0].firstChild.data
        if not isinstance(self.description, str):
            raise Exception('Illegal description')
        for i in range(1, len(children)):
            field_node = children[i]
            field_name = field_node.nodeName
            field = None
            if field_name == 'int':
                field = IntField(field_node)
            elif field_name == 'float':
                field = FloatField(field_node)
            elif field_name == 'bool':
                field = BoolField(field_node)
            elif field_name == 'string':
                field = StringField(field_node)
            elif field_name == 'list':
                field = ListField(field_node, objs)
            elif field_name == 'object':
                field = ObjectField(field_node, objs)
            self.fields[field.key] = field


class Object:
    """
    ObjectField和ObjectElement的共同基类
    """
    obj_class: Class


class ListField(Field):
    """
    对应xml中<list>
    """
    element: Element

    def __init__(self, xml: Any, objs: List[Tuple[str, Object]]) -> None:
        super().__init__(xml)
        children = xml.childNodes()
        if len(children) < 3:
            raise Exception('Illegal list field node')

        element_node = children[2]
        element_name = element_node.nodeName
        if element_name == 'int-element':
            self.element = IntElement(element_node)
        elif element_name == 'float-element':
            self.element = FloatElement(element_node)
        elif element_name == 'bool-element':
            self.element = BoolElement(element_node)
        elif element_name == 'string-element':
            self.element = StringElement(element_node)
        elif element_name == 'list-element':
            self.element = ListElement(element_node, objs)
        elif element_name == 'object-element':
            self.element = ObjectElement(element_node, objs)
        else:
            raise Exception('Illegal list element')


class ListElement(Element):
    """
    对应xml中<list-element>
    """
    element: Element

    def __init__(self, xml: Any, objs: List[Tuple[str, Object]]) -> None:
        super().__init__(xml)
        children = xml.childNodes()
        if len(children) < 2:
            raise Exception('Illegal list element node')

        element_node = children[1]
        element_name = element_node.nodeName
        if element_name == 'int-element':
            self.element = IntElement(element_node)
        elif element_name == 'float-element':
            self.element = FloatElement(element_node)
        elif element_name == 'bool-element':
            self.element = BoolElement(element_node)
        elif element_name == 'string-element':
            self.element = StringElement(element_node)
        elif element_name == 'list-element':
            self.element = ListElement(element_node, objs)
        elif element_name == 'object-element':
            self.element = ObjectElement(element_node, objs)
        else:
            raise Exception('Illegal list element')


class ObjectField(Field, Object):
    """
    对应xml中<object>
    """

    def __init__(self, xml: Any, objs: List[Tuple[str, Object]]) -> None:
        super(Field, self).__init__(xml)
        class_name = xml.getAttribute('class-name')
        if not isinstance(class_name, str):
            raise Exception(f'Illegal class name: {class_name}')
        objs.append((class_name, self))


class ObjectElement(Element, Object):
    """
    对应xml中<object-element>
    """
    obj_class: Class

    def __init__(self, xml: Any, objs: List[Tuple[str, Object]]) -> None:
        super(Element, self).__init__(xml)
        class_name = xml.getAttribute('class-name')
        if not isinstance(class_name, str):
            raise Exception(f'Illegal class name: {class_name}')
        objs.append((class_name, self))


class APIData:
    """
    对应xml中<api-data>
    """
    api_path: str
    type: str
    main_class: Class
    classes: Dict[str, Class]

    def __init__(self, xml: Any) -> None:
        objs: List[Tuple[str, Object]] = []
        self.classes = {}
        children = xml.childNodes()
        if children is None or len(children) < 3:
            raise Exception('Illegal api data')
        self.api_path = children[0].firstChild.data
        if not isinstance(self.api_path, str):
            raise Exception('Illegal api path')
        if not API_PATH.match(self.api_path):
            raise Exception(f'Illegal api path format: {self.api_path}')

        self.type = children[1].nodeName
        if self.type != 'http-request' and \
                self.type != 'http-response' and \
                self.type != 'ws-request' and \
                self.type != 'ws-response':
            raise Exception('Illegal api data type')

        self.main_class = Class(children[2], objs)

        if len(children) == 4:
            classes_node = children[3]
            if len(classes_node.childNodes()) == 0:
                raise Exception('Illegal classes')
            for class_node in classes_node.childNodes():
                class_var = Class(class_node, objs)
                self.classes[class_var.class_name] = class_var

        for obj_var in objs:
            obj_name = obj_var[0]
            obj = obj_var[1]
            if obj_name == self.main_class.class_name:
                obj.obj_class = self.main_class
            elif obj_name in self.classes:
                obj.obj_class = self.classes[obj_name]
            else:
                raise Exception(f'Class {obj_name} does not exist')