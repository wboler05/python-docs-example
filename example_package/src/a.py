#!/usr/bin/env python

'''
Prints MyClass with n=5
'''

from my_class import MyClass

def a():
  '''
  Prints sum of two arrays with n=5
  '''

  cls = MyClass(5)
  c = cls.calc()

  print('A: {}'.format(cls.a))
  print('B: {}'.format(cls.b))
  print('C: {}'.format(c))
