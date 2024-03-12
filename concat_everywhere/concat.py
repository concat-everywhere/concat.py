import inspect


def _smush(items):
    return { '_smush': items }


def concat(*terms):
    """
    Concatenates values and functions.
    """
    values = []
    for term in terms:
        sig = None

        if inspect.isfunction(term):
            sig = inspect.signature(term)
        elif inspect.isclass(term):
            sig = inspect.signature(term.__init__)

        if sig is None:
            values.append(term)
            continue

        n_args = len(sig.parameters)
        if n_args == 0:
            args = []
        else:
            args = values[-n_args:]
            values = values[0:-n_args]

        result = term(*args)

        if result is None:
            pass
        elif hasattr(result, '_smush'):
            values += result['_smush']
        else:
            values.append(result)

    return values
