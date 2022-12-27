from ranged import Range

MIN = 0
MAX = 10*6

def test_01():
    assert list(Range(MIN, MAX)) == list(range(MIN, MAX))

def test_func():
    assert ([i*2 for i in range(MIN, MAX)] == 
            list(Range(MIN, MAX, func=lambda x:x*2)))

def test_filt():
    assert ([i for i in range(MIN, MAX) if i%2 == 0] == 
            list(Range(MIN, MAX, filt=lambda x:x%2 == 0)))
