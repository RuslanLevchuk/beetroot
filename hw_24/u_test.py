from t_converter import converter
import unittest
import ass_test


class TempConvTest(unittest.TestCase):
    def test_f_to_c_1(self):
        self.assertEqual(converter('51F'), (11, 'C', '11C'))

    def test_f_to_c_2(self):
        self.assertEqual(converter('-2F'), (-19, 'C', '-19C'))

    def test_f_to_c_3(self):
        self.assertEqual(converter('67F'), (19, 'C', '19C'))

    def test_f_to_c_4(self):
        self.assertEqual(converter('52F'), (11, 'C', '11C'))

    def test_f_to_c_5(self):
        self.assertEqual(converter('8F'), (-13, 'C', '-13C'))

    def test_c_to_f_1(self):
        self.assertEqual(converter('-14C'), (7, 'F', '7F'))

    def test_c_to_f_2(self):
        self.assertEqual(converter('2C'), (36, 'F', '36F'))

    def test_c_to_f_3(self):
        self.assertEqual(converter('24C'), (75, 'F', '75F'))

    def test_c_to_f_4(self):
        self.assertEqual(converter('31C'), (88, 'F', '88F'))

    def test_c_to_f_5(self):
        self.assertEqual(converter('-15C'), (5, 'F', '5F'))

    def test_value_error(self):
        self.assertRaises(ValueError, converter, 'k')

    def test_ass_test(self):
        unittest.FunctionTestCase(ass_test.ass_test)


if __name__ == '__main__':
    unittest.main()