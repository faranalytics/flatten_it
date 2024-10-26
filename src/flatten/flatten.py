import typing


mappables = {dict}
sequentials = {list}


def flatten(it=None, sep=".") -> typing.Any:

    global mappables, sequentials

    _mappables = tuple(mappables)
    _sequentials = tuple(sequentials)

    ot = {}

    if isinstance(it, _mappables):
        stack = list(it.items())[::-1]
    elif isinstance(it, _sequentials):
        stack = list(enumerate(it))[::-1]

    while stack:

        head = stack.pop()

        if isinstance(head[1], _mappables):
            stack = stack + [(f"{head[0]}{sep}{item[0]}", item[1]) for item in head[1].items()][::-1]
        elif isinstance(head[1], _sequentials):
            stack = stack + [(f"{head[0]}{sep}{item[0]}", item[1]) for item in enumerate(head[1])][::-1]
        else:
            ot[head[0]] = head[1]

    return ot
