import importlib
from functools import wraps

import wifiphisher.common.constants


def uimethod(func):
    def _decorator(data, *args, **kwargs):
        return func(data, *args, **kwargs)

    func.is_uimethod = True
    return wraps(func)(_decorator)
