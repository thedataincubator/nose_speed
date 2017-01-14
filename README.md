## To Run
```bash
make test-split
make test-share
make test-bare
```

## Results


```
nose_speed$ make test-split
nosetests --processes=2 "test_split.py"
Setup Class
setUp
tearDown
setUp
tearDown
setUp
tearDown
setUp
tearDown
Teardown Class
....
----------------------------------------------------------------------
Ran 4 tests in 2.073s

OK
nose_speed$ make test-share
nosetests --processes=2 "test_share.py"
Setup Class
setUp
tearDown
setUp
tearDown
setUp
tearDown
setUp
tearDown
....Teardown Class

----------------------------------------------------------------------
Ran 4 tests in 2.061s

OK
nose_speed$ make test-bare
nosetests --processes=2 "test_bare.py"
Setup Class
setUp
tearDown
setUp
tearDown
setUp
tearDown
setUp
tearDown
Teardown Class
....
----------------------------------------------------------------------
Ran 4 tests in 2.050s

OK
```