import unittest
import time
import sys

class ShareTests(unittest.TestCase):
  _multiprocess_shared_ = True

  @classmethod
  def setup_class(cls):
    sys.stderr.write("Setup Class\n")
    time.sleep(1)  # slow setup

  @classmethod
  def teardown_class(cls):
    sys.stderr.write("Teardown Class\n")
    time.sleep(1)  # slow setup

  def setUp(self):
    sys.stderr.write("setUp\n")

  def tearDown(self):
    sys.stderr.write("tearDown\n")

  def test1(self):
    self.assertTrue(True)

  def test2(self):
    self.assertTrue(True)

  def test3(self):
    self.assertTrue(True)

  def test4(self):
    self.assertTrue(True)
