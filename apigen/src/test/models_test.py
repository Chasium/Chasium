"""
测试models
"""
import os
from unittest import TestCase
from xml.dom.minidom import parse
from src.models import APIData


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
