import sys
from fixtures import Fixtures

class TestA(Fixtures):
  _multiprocess_split_ = True

  def test1(self):
    sys.stderr.write("test1\n")
    self.assertTrue(self.setup)

  def test2(self):
    sys.stderr.write("test2\n")
    self.assertTrue(self.setup)

  def test3(self):
    sys.stderr.write("test3\n")
    self.assertTrue(self.setup)

  def test4(self):
    sys.stderr.write("test4\n")
    self.assertTrue(self.setup)
