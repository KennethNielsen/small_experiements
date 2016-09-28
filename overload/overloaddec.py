


from collections import defaultdict
from operator import itemgetter
from functools import wraps
import inspect

OVERLOAD = defaultdict(dict)

def overload(function):
    """Returns a function that will swicth depending on calling convention"""
    name = function.__name__
    # Get the annotations and turn the into a hashable type and save
    # this function under that key
    annotations = function.__annotations__
    annotation_key = tuple(sorted(annotations.items(), key=itemgetter(0)))
    OVERLOAD[name][annotation_key] = function

    # Store the positional argument names
    signature = inspect.signature(function)
    OVERLOAD[name]['arg_names'] = [str(arg) for arg in signature.parameters]

    @wraps(function)
    def wrapped(*args, **kwargs):
        # Form the calling signature of this call
        arg_names = OVERLOAD[name]['arg_names']
        # E.g: {'a': <class 'str'>, 'b': <class 'str'>}
        mykwargs = {k: type(v) for k, v in zip(arg_names, args)}
        for key, value in kwargs.items():
            mykwargs[key] = type(value)

        # Turn it into a hashable type and get the function
        annotation_key = tuple(sorted(mykwargs.items(), key=itemgetter(0)))
        try:
            this_overload = OVERLOAD[name][annotation_key]
        except KeyError:
            message = "Unknow overload for function '{}' with argument types: {}"
            raise TypeError(message.format(name, annotation_key))
        return this_overload(*args, **kwargs)

    return wrapped

