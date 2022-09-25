"""
生成器
"""
import os
from xml.dom.minidom import parse
from src.models import APIData, ModelsException

from src.py_model import PyModel
from src.ts_model import TsModel


class Generator:
    """
    生成器类
    """
    PY_PATH: str = '../backend'
    TS_PATH: str = '../frontend/src'

    def generate(self, xml_path: str, output_path: str) -> None:
        """
        生成一个ts文件和一个py文件
        """
        # 解析xml_path代表的xml文件，并用其根节点为参数创建APIData
        xml = parse(os.path.abspath(os.curdir + '/' + xml_path))
        xml_data = APIData(xml.childNodes[1])

        # 调用PyModel，在{后端根目录}/generated/{output_path}下创建一个py文件
        py_xml = PyModel(xml_data)
        py_path = self.PY_PATH + "/generated/" + output_path
        if os.path.isdir(py_path):
            pass
        else:
            os.makedirs(py_path)
        py_file = open(py_path + "/" + py_xml.class_name() +
                       ".py", "w", encoding='utf-8')
        py_file.write(py_xml.content())
        py_file.close()

        # 调用TsModel，在{前端根目录}/src/generated/{output_path}下创建一个ts文件
        ts_xml = TsModel(xml_data)
        ts_path = self.TS_PATH + "/generated/" + output_path
        if os.path.isdir(ts_path):
            pass
        else:
            os.makedirs(ts_path)
        ts_xml = TsModel(xml_data)
        ts_file = open(ts_path + "/" + ts_xml.class_name() +
                       ".ts", "w", encoding='utf-8')
        ts_file.write(ts_xml.content())
        ts_file.close()
