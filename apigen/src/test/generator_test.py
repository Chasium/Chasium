"""
测试generator
"""
from unittest import TestCase, mock


class TestGenerator(TestCase):
    """
    测试generator
    """

    def test_generate(self):
        """
        测试generator
        """
        from src.generator import Generator  # pylint:disable=import-outside-toplevel
        generator = Generator()
        generator.generate("apis/test/test2.xml", "qqwwee")
        '''
        with mock.patch('src.ts_model.TsModel') as mock_ts:
            with mock.patch('src.py_model.PyModel') as mock_py:
                mock_ts_model = mock_ts.return_value
                mock_ts_model.class_name.return_value = 'A'
                mock_ts_model.content.return_value = 'aaaaa'
                mock_py_model = mock_py.return_value
                mock_py_model.class_name.return_value = 'B'
                mock_py_model.content.return_value = 'bbbbb'
                from src.generator import Generator  # pylint:disable=import-outside-toplevel
                generator = Generator()
                generator.generate("apis/test/test.xml", "qqwwee")
                f = open(generator.TS_PATH + "/generated/" +
                         "qqwwee" + "/" + "B" + ".py", encoding='utf-8')
                self.assertEqual(f.read(), 'bbbbb')
                f.close()
                f = open(generator.TS_PATH + "/generated/" +
                         "qqwwee" + "/" + "A" + ".ts", encoding='utf-8')
                self.assertEqual(f.read(), 'aaaaa')
                f.close()
        '''
