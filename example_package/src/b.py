#!/usr/bin/env python

'''
Prints MyClass with n=10
'''

from .my_class import MyClass

def b():
  '''
  Prints sum of two arrays with n=10
  '''

  cls = MyClass(10)
  c = cls.calc()
  cls.print()

  print('A: {}'.format(cls.a))
  print('B: {}'.format(cls.b))
  print('C: {}'.format(c))
