import unittest

def convert_SI_lenghth(val, unit_in, unit_out):
    SI = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000.}
    return val*SI[unit_in]/SI[unit_out]

def convert_SI_weight(val, unit_in, unit_out):
    SI = {'mg':0.001, 'cg':0.01, 'g':1.0, 'kg':1000.}
    return val*SI[unit_in]/SI[unit_out]

class TestMeasurements(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(convert_SI_weight(10000,mg,kg), 0.01)

    def test_upper(self):
        self.assertEqual(convert_SI_weight(100 ,kg,g), 100000)

    def test_upper(self):
        self.assertEqual(convert_SI_weight(100 ,g,mg), 100000)

    def test_upper(self):
        self.assertEqual(convert_SI_lenghth(50,km,m), 50000)

    def test_upper(self):
        self.assertEqual(convert_SI_lenghth(20,mm,m), 0,02)
if __name__ == '__main__':
    unittest.main()


