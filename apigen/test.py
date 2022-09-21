"""
单元测试的入口类
"""
import unittest
from src.test.models_test import TestModels
from src.test.generator_test import TestGenerator


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([
        TestModels("test_from_valid"),
        TestModels("test_from_invalid")
    ])

    suite.addTests([
        TestGenerator("test_generate")
    ])

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
