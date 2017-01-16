def check(i):
  assert i % 2 == 0

def test1():
  for i in xrange(10):
    yield check, i

def test2():
  for i in xrange(10):
    yield check, i
