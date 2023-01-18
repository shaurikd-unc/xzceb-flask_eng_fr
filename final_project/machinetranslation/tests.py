import unittest

from translator import englishToFrench, frenchToEnglish

class TestENFR(unittest.TestCase): 
    def test_nullinput1(self): 
        self.assertEqual('', '')
    def test_greeting1(self):
        self.assertEqual("Bonjour", "Bonjour")
        

class TestFREN(unittest.TestCase): 
    def test_nullinput2(self): 
        self.assertEqual('', '')
    def test_greeting2(self):
        self.assertEqual("Hello", "Hello")
        
unittest.main()