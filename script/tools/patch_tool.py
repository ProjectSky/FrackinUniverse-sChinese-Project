import json
import os
import re
from codecs import open as open_n_decode
from json_tools import field_by_path, list_field_paths, prepare


def add_value(dict_obj, path, value):
    obj = dict_obj
    for i, v in enumerate(path):
        if i + 1 == len(path):
            if not isinstance(obj.get(v, ''), list):
                obj[v] = list()
            obj[v].append(value)
            continue
        obj[v] = obj.get(v, '') or dict()
        obj = obj[v]
    return dict_obj


def op_select(jsons):
    index = 0
    json_text = json.loads(jsons)
    op_list = list()
    i_list = list()
    result = list()
    for i, value in enumerate(json_text):
        op_result = value['op']
        op_list.append(op_result)
        i_list.append(i)
    op_dict = list(zip(i_list, op_list))
    for value in op_dict:
        if list(op_dict[index])[1] == 'remove' or list(op_dict[index])[1] == 'test':
            pass
        else:
            result.append(list(op_dict[index])[0])
        index = index+1
    return result


def trans_patch(jsons):
    string = prepare(jsons)
    json_text = json.loads(string)
    value_list = list()
    path_list = list()
    op_list = op_select(string)
    result1 = {}
    for i, value in enumerate(json_text):
        for op in op_list:
            value_result = list(list(enumerate(json_text))[op])[1]['value']
            path_result = list(list(enumerate(json_text))[op])[1]['path'].split('/')
            path_result = [i for i in path_result if(len(str(i)) != 0)]
            value_list.append(value_result)
            path_list.append(path_result)
    dict_result = zip(path_list, value_list)
    for path, value in dict_result:
        add_value(result1, path, value)
        result2 = json.dumps(result1).replace('\\', "")
    return str(result2)


def trans_patch_no_op(jsons):
    string = prepare(jsons)
    json_text = json.loads(string)
    value_list = list()
    path_list = list()
    result1 = {}
    for i, value in enumerate(json_text):
        value_result = value['value']
        path_result = str(value['path']).split('/')
        path_result = [i for i in path_result if(len(str(i)) != 0)]
        value_list.append(value_result)
        path_list.append(path_result)
        dict_result = zip(path_list, value_list)
    for path, value in dict_result:
        add_value(result1, path, value)
        result2 = json.dumps(result1).replace('\\', "")
    return str(result2)


if __name__ == "__main__":
    jsons3 = open_n_decode(
        'F:/FrackinUniverse - patch/playermodes.config.patch', "r", "utf_8_sig")
    test = trans_patch(jsons3)
    print(test)
