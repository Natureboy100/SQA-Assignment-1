import unittest
import Main

class TestMeasurements(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Main.convert_SI_weight(10000,'mg','kg'), 0.01)

    def test_2(self):
        self.assertEqual(Main.convert_SI_weight(100 ,'kg','g'), 100000)

    def test_3(self):
        self.assertEqual(Main.convert_SI_weight(100 ,'g','mg'), 100000)

    def test_4(self):
        self.assertEqual(Main.convert_SI_lenghth(50,'km','m'), 50000)


    def test_5(self):
        self.assertEqual(Main.convert_SI_lenghth(20,'mm','m'), 0.022) #deliberate error creation

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMeasurements('test_1'))
    suite.addTest(TestMeasurements('test_2'))
    suite.addTest(TestMeasurements('test_3'))
    suite.addTest(TestMeasurements('test_4'))
    suite.addTest(TestMeasurements('test_5'))
    return suite
suite1 = unittest.TestLoader().loadTestsFromTestCase(TestMeasurements)


if __name__ == '__main__':
    unittest.main()

