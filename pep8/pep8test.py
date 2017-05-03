#!/usr/bin/python

""" Sample pep8 style guide test """

import os
import sys

def sample_function(arg1, arg2):

    '''
    sample function
    '''

    print "SampleFunction"
    print os.name
    print arg1
    print arg2


def sample_next_function(arg1, arg2, arg3, arg4,
                         arg5):

    '''
    sample next function
    '''

    print "sample next function"
    print sys.copyright
    first_var = arg1
    second_var = arg2
    third_var = arg3
    fourth_var = arg4
    fifth_var = arg5
    print first_var
    print second_var
    print third_var
    print fourth_var
    print fifth_var
