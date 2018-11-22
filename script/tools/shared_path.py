from os.path import split as splitpath
from os.path import join


def splitfullpath(path):
    if len(path) == 0:
        return list()
    head, tail = splitpath(path)
    base = splitfullpath(head)
    base.append(tail)
    return base


def getSharedPart(strings, minlength=3):
    if len(strings) == 1:
        return strings[0]
    if len(strings) == 0:
        raise Exception("Empty argument passed to getSharedPart")
    firstlen = len(strings[0])
    for ethalonlen in range(firstlen, minlength - 1, -1):
        for offset in range(0, firstlen - ethalonlen + 1):
            ethalon = strings[0][offset:offset + ethalonlen]
            # print("Ethalon = " + ethalon)
            found = True
            for s in strings:
                if s.find(ethalon) == -1:
                    found = False
                    break
            if found:
                return "shared_" + ethalon
    return "."


def getSharedPath(files):
    splitedfiles = list()
    for f in files:
        splitedfiles.append(splitfullpath(f))
    i = 0
    variants = list()
    result = ""
    while len(variants) > 0 or i == 0:
        variants = list()
        for f in splitedfiles:
            if i >= len(f):
                variants = list()
                break
            token = f[i]
            if token not in variants:
                variants.append(token)
        if len(variants) == 0:
            break
        else:
            result = join(result, getSharedPart(variants))
        i += 1
    return result
