import sys

_multiprocess_can_split_ = True

called = []

def setup():
  sys.stderr.write("setup called\n")
  called.append("setup")

def teardown():
  sys.stderr.write("teardown called\n")
  called.append("teardown")

def test1():
  sys.stderr.write("testing 1\n")
  assert len([x for x in called if x == "setup"]) == 1

def test2():
  sys.stderr.write("testing 2\n")
  assert len([x for x in called if x == "setup"]) == 1
