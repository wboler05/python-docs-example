#!/usr/bin/env python

import numpy as np

class MyClass(object):
  '''
  A class that randomly generates 2 arrays and adds them together.
  '''

  def __init__(self, n=5):
    '''
    Instantiates two arrays

    @param n : int : size of arrays
    '''
    self.a = np.random.sample(n)
    self.b = np.random.sample(n)

  def calc(self):
    '''
    Adds two arrays a and b and returns sum

    @return : np.array : Sum of 'a' + 'b'
    '''
    return self.a + self.b


