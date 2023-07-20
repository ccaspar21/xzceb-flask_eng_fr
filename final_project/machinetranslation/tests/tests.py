import unittest
from translator import english_to_french, french_to_english

class TestTranslateEnglishToFrench(unittest.TestCase):
  def test1(self):
    self.assertEqual(english_to_french("Hello"), "Bonjour")
    self.assertNotEqual(english_to_french("Bonjour"), "English")

class TestTranslateFrenchToEnglish(unittest.TestCase):
  def test1(self):
    self.assertEqual(french_to_english("Hello"), "Bonjour")
    self.assertNotEqual(french_to_english("Bonjour"), "English")

unittest.main()
