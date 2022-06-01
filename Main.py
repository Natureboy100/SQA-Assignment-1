import unittest

def convert_SI_lenghth(val, unit_in, unit_out):
    SI = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000.}
    return val*SI[unit_in]/SI[unit_out]

def convert_SI_weight(val, unit_in, unit_out):
    SI = {'mg':0.001, 'cg':0.01, 'g':1.0, 'kg':1000.}
    return val*SI[unit_in]/SI[unit_out]



