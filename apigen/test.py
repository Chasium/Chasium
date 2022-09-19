"""
单元测试的入口类
"""
import unittest
from src.test.models_test import TestModels


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([
        TestModels("test_from_valid"),
        TestModels("test_from_invalid")
    ])

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
