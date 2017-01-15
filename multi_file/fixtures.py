import unittest
import sys
import time

class Fixtures(unittest.TestCase):
  @classmethod
  def setup_class(cls):
    cls.setup = True
    sys.stderr.write("Setup Class\n")
    time.sleep(1)  # slow setup

  @classmethod
  def teardown_class(cls):
    sys.stderr.write("Teardown Class\n")
    time.sleep(1)  # slow setup
