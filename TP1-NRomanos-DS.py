import unittest

def decimal_to_roman(decimal):
    if decimal <= 1:
        return "I"* decimal
    elif decimal == 2:
        return "II"
    elif decimal == 5:
        return "V" 
    else:
        return "X" 
    if decimal == 50:
        return "L"
    elif decimal ==100:
        return "C"



class TestDecimalToRoman (unittest.TestCase):
    def test_1(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, "I")

    def test_10(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, "X")

    def test_5(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado,"V")

    def test_2(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, "II") 

    def test_3(self):
        resultado = decimal_to_roman(3)
        self.assertEqual (resultado, "III")

    def test_4(self):
        resultado= decimal_to_roman(4)
        self.assertEqual(resultado, "IV")

    def test_6(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, "VI")

    def test_10(self):
        resultado= decimal_to_roman (10)
        self.assertEqual(resultado, "X")
        
    def test_15(self):
        resultado = decimal_to_roman(15)
        self.assertEqual(resultado, "XV")

    def test_20(self):
        resultado = decimal_to_roman(20)
        self.assertEqual(resultado, "XX")

    def test_50(self):
        resultado = decimal_to_roman(50)
        self.assertEqual(resultado, "L")

    def test_100(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, "C")

    def test_150(self):
        resultado = decimal_to_roman(150)
        self.assertEqual(resultado, "CL")

    
if __name__== "__main__":
    unittest.main() 
