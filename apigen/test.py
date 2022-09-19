"""
单元测试的入口类
"""
import unittest
from src.test.models_test import TestModels


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestModels("test_from_valid"))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
