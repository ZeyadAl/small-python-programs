from functools import reduce
flatten = lambda lst: reduce((lambda x, y: x+y),lst)
