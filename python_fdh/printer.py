

from pyfdh_types import Symbol


def pr_str(val):
    if val is None:
        return None
    if isinstance(val, Symbol):
        return val.name
    if isinstance(val, int):
        return str(val)
    if isinstance(val, list):
        repred = ' '.join([pr_str(inside) for inside in val])
        return '(' + repred + ')'
    raise Exception('not able to print object %s of type %s' % (val, type(val)))
