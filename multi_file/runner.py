import unittest
from test_a import TestA
from test_b import TestB

# def get_tests(obj, prefix="test"):
#   return [m for m in dir(obj) if callable(getattr(obj, m)) and m.startswith(prefix)]

def main():
  suite = unittest.TestSuite()
  loader = unittest.TestLoader()
  suite.addTests(loader.loadTestsFromTestCase(TestA))
  suite.addTests(loader.loadTestsFromTestCase(TestB))
  unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
  main()
