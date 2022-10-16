"""
入口文件
"""
import re
import glob
import sys
from src.models import ModelsException
from src.generator import Generator

TEST_PATH = re.compile(r'apis\\test\\')
XML_PATH = re.compile(r'.*\.xml')

if __name__ == "__main__":
    # 遍历apis目录下除test目录外的所有xml文件，调用Generator为它们生成对应的ts和py文件
    f = []
    if len(sys.argv) > 1:
        for i in sys.argv:
            if XML_PATH.match(i):
                f += glob.glob(f"apis/{i}")
    else:
        f = glob.glob("apis/**/*.xml")
    if f is not None:
        for file in f:
            if TEST_PATH.match(file) is None:
                print(file)
                xml_file = Generator()
                try:
                    xml_file.generate(file, file[5:])
                except ModelsException as e:
                    print(e)
