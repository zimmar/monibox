# Python3 program to convert string
# from camel case to snake case

def camel_to_snake(cts):
    res = [cts[0].lower()]
    for c in cts[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)

    return ''.join(res)


# from snake case to camel case
def snake_to_camel(stc):
    res = []
    UP = 1
    for c in stc:
        if c == '_':
            UP = 1
        else:
            if (UP == 1) and (c in ('abcdefghijklmnopqrstuvwxyz')):
                res.append(c.upper())
                UP = 0
            else:
                res.append(c)

    return ''.join(res)