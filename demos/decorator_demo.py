# -*- coding: utf-8 -*-
# decorator的运用
import functools

import functools

def log(param):
    if hasattr(param,'__call__'):
        @functools.wraps(param)
        def warpper(*args, **kw):
            print('begin call')
            _rsFunc = param(*args, **kw)
            print('after call')
            return _rsFunc
        return warpper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin call')
                print(param)
                _rsFunc = func(*args, **kw)
                print('after call')
                return _rsFunc
            return wrapper
        return decorator
@log('1')
def nums():
	print ('111111')
nums()