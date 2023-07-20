from deep_translator import MyMemoryTranslator

def english_to_french(eng_text_input):
  """
  Converts english to french
  """
  fr_text_output = MyMemoryTranslator(source='english',target='french').translate(eng_text_input)
  return fr_text_output

def french_to_english(fr_text_input):
  """
  Converts english to french
  """
  eng_text_output = MyMemoryTranslator(source='french',target='english').translate(fr_text_input)
  return eng_text_output
  
