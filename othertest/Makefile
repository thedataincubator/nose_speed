test-single:
	nosetests -v test_not_shared.py
	nosetests -v test_shared.py
	nosetests -v test_can_split.py

test-double:
	nosetests -v --processes=2 test_not_shared.py
	nosetests -v --processes=2 test_shared.py
	nosetests -v --processes=2 test_can_split.py
