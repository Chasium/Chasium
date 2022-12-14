"""
测试pyModel和TsModel的content函数返回值
"""
import os
from unittest import TestCase
from xml.dom.minidom import parse
from src.py_model import PyModel
from src.ts_model import TsModel
from src.models import APIData


class TestContent(TestCase):
    """
    测试pyModel和TsModel的content函数返回值
    """

    def test_content(self):
        """
        测试pyModel和TsModel的content函数返回值
        """
        xml = parse(os.path.abspath(os.curdir + '/apis/test/test.xml'))
        xml_data = APIData(xml.childNodes[1])

        py_content = PyModel(xml_data).content()
        py_file = open(os.path.abspath(os.curdir + '/src/test/Test.py'), 'w')
        py_file.write(py_content)
        py_file.close()
        # 验证生成的python文件的有效性
        try:
            from src.test.Test import Test, Test1  # pylint:disable=import-outside-toplevel
        except ImportError:
            self.fail()

        ts_content = TsModel(xml_data).content()
        ts_file = open(os.path.abspath(os.curdir + '/src/test/Test.ts'), 'w')
        ts_file.write(ts_content)
        ts_file.close()
        # 不知道怎么验证ts文件的有效性
