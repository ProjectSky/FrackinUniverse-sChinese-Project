import json
import os
import re
from codecs import open as open_n_decode
from json_tools import field_by_path, list_field_paths, prepare

##网上抄的函数，用来合成json，结果还算可靠
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

## 稳定筛选文本的必要函数，原理是将文本所在的索引值提取出来
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

## 绝对可靠的扫描方式之一，但是效率过低，目前只对带remove和test的文件使用
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

###正常的扫描方式，针对普通的patch
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
        result2 = json.dumps(result1).replace('\\', "").replace(': [{"',': {"').replace('}]','}')
    return str(result2)

###fuck utf8 bom!(未完成)
def fuck_utf8_bom(jsons):
    print(str(jsons))
    u = str(jsons).decode('utf-8-sig') 
    s = u.encode('utf-8') 
    return s
     
 


if __name__ == "__main__":
    jsons3 = open_n_decode(
        'F:/FrackinUniverse/dialog/converse.config.patch', "r", "utf_8_sig")
    test = trans_patch_no_op(jsons3)
    print(test)

