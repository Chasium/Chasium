"""
入口文件
"""
import re
import glob
from src.generator import Generator

TEST_PATH = re.compile(r'apis\\test\\')

if __name__ == "__main__":
    # 遍历apis目录下除test目录外的所有xml文件，调用Generator为它们生成对应的ts和py文件
    f = glob.glob("apis/**/*.xml")
    for file in f:
        if TEST_PATH.match(file) is None:
            print(file)
            xml_file = Generator()
            xml_file.generate(file, file[5:])
