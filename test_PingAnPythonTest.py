import unittest
from PingAnPythonTest import reverseInput

# Input:
input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}
 
# Output:
output_value = {
  'I': {
    'deserve': {
      'to': {
         'be': 'hired'
      }
    }
  }
}

class TestStringMethods(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test_simple(self):
        dic={'A':'B'}
        result=reverseInput(dic)
        self.assertEqual(result,{'B':'A'})
    def test_multiple(self):
        result=reverseInput(input_value)
        self.assertEqual(result,output_value)
unittest.main()