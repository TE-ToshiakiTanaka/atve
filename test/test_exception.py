from nose.tools import with_setup, raises, ok_, eq_, timed
from atve.exception import *

def setup():
    pass

def teardown():
    pass

@with_setup(setup, teardown)
def test_exception_error_01():
    try: raise AtveError()
    except AtveError as a: fail()
    except TypeError as t:
        ok_(True)

@with_setup(setup, teardown)
def test_exception_error_02():
    try: raise AtveError("hoge")
    except AtveError as a: fail()
    except Exception as e:
        eq_(str(e), "AtveError : details must be a dictionary")

@with_setup(setup, teardown)
def test_exception_error_03():
    try: raise AtveError({
        1  : "hoge"
    })
    except AtveError as a: fail()
    except Exception as e:
        eq_(str(e), 'AtveError : details key must be strings')

@with_setup(setup, teardown)
def test_exception_error_04():
    try: raise AtveError({
        'hoge'  : "hoge"
    })
    except AtveError as a: fail()
    except Exception as e:
        eq_(str(e), 'AtveError : details must have mesage field')

@with_setup(setup, teardown)
def test_exception_error_05():
    try: raise AtveError({
        'message'  : "test"
    })
    except AtveError as a:
        eq_(a.__getattr__('type'), type(a).__name__)

@with_setup(setup, teardown)
def test_exception_error_06():
    try: raise AtveError({
        'message'  : "test",
    })
    except AtveError as a:
        eq_(a.print_trace(), None)
