"""
入口文件
"""
import re
import shutil
import glob
import sys
import os
from src.models import ModelsException
from src.generator import Generator

TEST_PATH = re.compile(r'apis[\\/]test[\\/]')
XML_PATH = re.compile(r'.*\.xml')
XML2_PATH = re.compile(r'[\\/].*?\.xml$')

if __name__ == "__main__":
    # 遍历apis目录下除test目录外的所有xml文件，调用Generator为它们生成对应的ts和py文件
    f = []
    if len(sys.argv) > 1:
        for i in sys.argv:
            if XML_PATH.match(i):
                f += glob.glob(f"apis/{i}")
    else:
        f = glob.glob("apis/**/*.xml")
        if os.path.isdir(Generator.PY_PATH + '/generated'):
            shutil.rmtree(Generator.PY_PATH + '/generated')
        if os.path.isdir(Generator.TS_PATH + '/generated'):
            shutil.rmtree(Generator.TS_PATH + '/generated')

    if f is not None:
        for file in f:
            if TEST_PATH.match(file) is None:
                print(file)
                xml_file = Generator()
                try:
                    output_path = XML2_PATH.sub('', file[5:])
                    xml_file.generate(file, output_path)
                except ModelsException as e:
                    print(e)
