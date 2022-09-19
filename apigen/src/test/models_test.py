"""
测试models
"""
import os
from unittest import TestCase
from xml.dom.minidom import parse
from src.models import APIData, ModelsException  # pylint:disable=import-error (为什么？？)


class TestModels(TestCase):
    """
    测试models
    """

    def test_from_valid(self):
        """
        从有效的xml文档测试models
        """
        xml = parse(os.path.abspath(os.curdir + '/apis/test/test.xml'))
        test_data = APIData(xml.childNodes[1])
        self.assertEqual(test_data.main_class.class_name, 'Test')
        self.assertTrue(test_data.main_class.fields['a1'] is not None)
        self.assertTrue(
            test_data.main_class.fields['a2'].element.element.obj_class.fields['aAbBcCDDe'] is not None
        )

    def test_from_invalid(self):
        """
        从无效的xml文档测试models
        """
        try:
            xml = parse(os.path.abspath(os.curdir + '/apis/test/wrong.xml'))
            test_data = APIData(xml.childNodes[1])
            self.assertEqual(test_data.main_class.class_name, 'Test')
            self.fail()
        except ModelsException as err:
            self.assertEqual(str(err), 'Class Test2 does not exist')
