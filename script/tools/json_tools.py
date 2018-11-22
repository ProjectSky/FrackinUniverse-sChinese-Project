separator = {"basic": "\n", "string": "\\n", "comment": ""}


def parse_line(line, prev_state):
    result = ""
    offset = 0
    state = prev_state
    while offset < len(line):
        c = line[offset]
        if state != "comment":
            if state == "basic" and c == '/' and offset + 1 < len(line):
                if line[offset + 1] == "*":
                    state = "comment"
                    offset += 1
                elif line[offset + 1] == "/":
                    break
            else:
                if state == "string" and c == '\\':
                    result += c
                    result += line[offset + 1]
                    offset += 2
                    continue
                if c not in ['\n', '\r']:
                    result += c
                if c == '"':
                    if state == "string":
                        state = "basic"
                    elif state == "basic":
                        state = "string"
        else:
            if c == "*" and offset + 1 < len(line):
                if line[offset + 1] == "/":
                    state = "basic"
                    offset += 1
        offset += 1
    return result + separator[state], state


def prepare(source):
    result = ""
    state = "basic"
    for line in source:
        newline, state = parse_line(line, state)
        result += newline
    return result


def list_field_paths(obj, sep="/"):
    result = list()
    if type(obj) is dict:
        for field, val in obj.items():
            if type(val) is dict or type(val) is list:
                subfields = list_field_paths(val, sep)
                for subfield in subfields:
                    result.append(field + sep + subfield)
            else:
                result.append(field)
    elif type(obj) is list:
        for i, val in enumerate(obj):
            field = str(i)
            if type(val) is dict or type(val) is list:
                subfields = list_field_paths(val, sep)
                for subfield in subfields:
                    result.append(field + sep + subfield)
            else:
                result.append(field)
    return result


def field_by_path(obj, path, newval=None, sep="/"):
    offset = path.find(sep)
    if offset == -1:
        index = path
        if type(obj) is list:
            index = int(path)
        if not newval is None:
            obj[index] = newval
        oldval = obj[index]
        return oldval
    field = path[:offset]
    if type(obj) is list:
        field = int(field)
    rest = path[offset + len(sep):]
    if (not newval is None) and (field not in obj):
        obj[field] = dict()
    return field_by_path(obj[field], rest, newval=newval, sep=sep)
