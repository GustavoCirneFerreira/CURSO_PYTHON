class MyError(Exception):
    ...

class OutroError(Exception):
    ...

def levantar():
    exception_ = MyError('a', 'b', 'c')
    raise exception_

try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar dnv')
    raise exception_ from error