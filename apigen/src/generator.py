"""
生成器
"""
from src.models import APIData


class Generator:
    """
    生成器类
    """

    def generate(self, xml_path: str, output_path: str) -> None:
        """
        生成一个ts文件和一个py文件
        """
        # TODO: 解析xml_path代表的xml文件，并用其根节点为参数创建APIData
        # TODO: 调用TsModel，在{前端根目录}/src/generated/{output_path}下创建一个ts文件
        # TODO: 调用PyModel，在{后端根目录}/generated/{output_path}下创建一个py文件
