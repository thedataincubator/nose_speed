import sys
import unittest
from test_a import TestA
from test_b import TestB

def extract(obj, prefix="test"):
  return [obj(m) for m in dir(obj) if callable(getattr(obj, m)) and m.startswith(prefix)]

def main():
  suite = unittest.TestSuite()
  loader = unittest.TestLoader()
  for test in extract(TestA) + extract(TestB):
    suite.addTest(test)
  print >> sys.stderr, "foo"
  print >> sys.stderr, suite._tests
  unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
  print >> sys.stderr, "hi"
  main()
