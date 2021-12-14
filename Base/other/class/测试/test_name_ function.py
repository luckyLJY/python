import unittest

'''
assertEqual(a, b) 核实a == b
assertNotEqual(a, b) 核实a != b
assertTrue(x) 核实x为True
assertFalse(x) 核实x为False
assertIn(item, list) 核实item在list中
assertNotIn(item, list) 核实item不在list中
'''
from 测试.name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()