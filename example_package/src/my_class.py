#!/usr/bin/env python

'''
An example class that randomly generates two arrays
and adds them together.  It provides an example to show
with Doxygen and Sphinx, and does nothing special.
'''

import numpy as np

from .my_other_class import MyOtherClass

class MyClass(MyOtherClass):
  '''
  A class that randomly generates 2 arrays and adds them together.
  '''

  def __init__(self, n=5):
    '''
    Instantiates two arrays

    @param n size of arrays
    '''
    self.a = np.random.sample(n) # Does something
    self.b = np.random.sample(n) # Does something as well

  def calc(self):
    '''
    Adds two arrays a and b and returns sum

    @return np.array Sum of 'a' + 'b'
    '''
    self.c = self.a + self.b
    return self.c


