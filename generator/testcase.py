import unittest

class Test():
  def check(self, i):
    assert i % 2 == 0

  def test1(self):
    for i in xrange(10):
      yield self.check, i

  def test2(self):
    for i in xrange(10):
      yield self.check, i
