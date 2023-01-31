import unittest

from translator import englishToFrench, frenchToEnglish


class TestEF(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")  # test when "Hello" is given as input the output is "Bonjour".
        self.assertEqual(englishToFrench("door"), "Porte")  # test when "door" is given as input the output is "porte".
        self.assertEqual(englishToFrench("carpet"),"Tapis")  # test when "carpet" is given as input the output is "tapis".

    def test2(self):
        self.assertEqual(englishToFrench(None), "null input")  # test when no input is given as input the output is "null input".
        self.assertEqual(englishToFrench("three"),"Trois")  # test when "three" is given as input the output is "trois".
        self.assertEqual(englishToFrench("four"),"Quatre")  # test when "four" is given as input the output is "quatre".


class TestFE(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")  # test when "Bonjour" is given as input the output is "Hello".
        self.assertEqual(frenchToEnglish("porte"), "Door")  # test when "porte" is given as input the output is "door".
        self.assertEqual(frenchToEnglish("tapis"),"Carpets")  # test when "tapis" is given as input the output is "carpet".

    def test2(self):
        self.assertEqual(frenchToEnglish(None), "null input")  # test when no input given as input the output is "null input".
        self.assertEqual(frenchToEnglish("trois"),"Three")  # test when "trois" is given as input the output is "three".
        self.assertEqual(frenchToEnglish("quatre"),"Four")  # test when "quatre" is given as input the output is "four".


unittest.main()