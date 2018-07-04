# -*- coding: utf-8 -*-

import unittest

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score > 100 or self.score < 0:
            raise  ValueError("this score is wrong!")

        if self.score < 60:
            return 'C'

        if self.score < 80:
            return 'B'

        else:
            return 'A'

class TestStudent(unittest.TestCase):
    def test_80_to_100(self):
        s1 = Student('Bart',80)
        s2 = Student('List',100)
        self.assertEqual(s1.get_grade(),'A')
        self.assertEqual(s2.get_grade(),'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('List', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('List', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('List', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__=='__main__':
    unittest.main()
