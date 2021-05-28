#!/usr/bin/env python

'''
I want to add some complexity to our MyClass
'''

import numpy as np

class MyOtherClass(object):
    '''
    This is just another class that adds complexity to MyClass
    '''

    def __init__(self):
        self.c = None

    def print(self):
        '''
        Prints the internal self.c
        '''
        print("self.C: {}".format(self.c))
