import json
import os
import re
from codecs import open as open_n_decode
from json_tools import field_by_path, list_field_paths, prepare

# 网上抄的函数，用来合成json，结果还算可靠尼玛呢坑死我了


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

# 稳定筛选文本的必要函数，原理是将文本所在的索引值提取出来


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

# 绝对可靠的扫描方式，针对普通的patch，摒弃了繁琐的转换和词典筛选！


def trans_patch(jsons):
    string = prepare(jsons)
    json_text = json.loads(string)
    value_list = list()
    path_list = list()
    path_list_2 = list()
    value_list_2 = list()
    op_list = list()
    for i, value in enumerate(json_text):
        path_result = value['path']
        op_result = value['op']
        try:
            value_result = value['value']
        except:
            value_result = ''
        value_list.append(value_result)
        path_list.append(path_result)
        op_list.append(op_result)
        dict_result = tuple(zip(op_list, path_list, value_list))
    for i in dict_result:
        if i[0] == 'add' or i[0] == 'replace':
            path_1 = i[1]
            path_2 = list_field_paths(i[2])
            if path_2 == []:
                path_2 = ['*']
            else:
                pass
            for v in path_2:
                if path_2 == ['*']:
                    value = i[2]
                    path = path_1.replace('/', '', 1)
                    value_list_2.append(value)
                    path_list_2.append(path)
                else:
                    value = field_by_path(i[2], v)
                    path = (path_1+'/' + v).replace('/', '', 1)
                    value_list_2.append(value)
                    path_list_2.append(path)
        else:
            pass
    result = tuple(zip(path_list_2, value_list_2))
    return result


def to_a_list(tuple, no):
    re = list()
    for i in tuple:
        re.append(i[no])
    return re


# fuck utf8 bom!(未完成)
"""
def fuck_utf8_bom(jsons):
    print(str(jsons))
    u = str(jsons).decode('utf-8-sig') 
    s = u.encode('utf-8') 
    return s
"""


def trans_patch_spcial_1(jsons, ex):
    string = prepare(jsons)
    json_text = json.loads(string)
    value_list = list()
    path_list = list()
    path_list_2 = list()
    path_list_3 = list()
    value_list_2 = list()
    op_list = list()
    ex_list = ex
    for i, value in enumerate(json_text):
        path_result = value['path']
        op_result = value['op']
        try:
            value_result = value['value']
        except:
            value_result = ''
        value_list.append(value_result)
        path_list.append(path_result)
        op_list.append(op_result)
    """
    for i in ex_list:
        if i[2] == 1 :
            o = i[1]
            for text in path_list:
                if not re.search(i[0]+'/'+'-',text) == None :
                    wait = text.replace(i[0]+'/'+'-',i[0]+'/'+str(o))
                    path_list_3.append(wait)
                    o=o+1
                else:
                    path_list_3.append(text)
        else:
            for text in path_list:
                if not re.search(i[0]+'/'+'-',text) == None :
                    wait = text.replace(i[0]+'/-',i[0]+'/'+str(i[1]))
                    path_list_3.append(wait)
                else:
                    path_list_3.append(text)
        path_list = path_list_3  
    """
    for i in ex_list:
        path_list = replace_the_path(path_list, i)
    dict_result = tuple(zip(op_list, path_list, value_list))
    for i in dict_result:
        if i[0] == 'add' or i[0] == 'replace':
            path_1 = i[1]
            path_2 = list_field_paths(i[2])
            if path_2 == []:
                path_2 = ['*']
            else:
                pass
            for v in path_2:
                if path_2 == ['*']:
                    value = i[2]
                    path = path_1.replace('/', '', 1)
                    value_list_2.append(value)
                    path_list_2.append(path)
                else:
                    value = field_by_path(i[2], v)
                    path = (path_1+'/' + v).replace('/', '', 1)
                    value_list_2.append(value)
                    path_list_2.append(path)
        else:
            pass
    result = tuple(zip(path_list_2, value_list_2))
    return result


def replace_the_path(path, rule):
    path_list_3 = list()
    o = rule[1]
    for text in path:
        if rule[2] == 1:
            if not re.search(rule[0]+'/'+'-', text) == None:
                wait = text.replace(rule[0]+'/'+'-', rule[0]+'/'+str(o))
                path_list_3.append(wait)
                o = o+1
            else:
                path_list_3.append(text)
        else:
            if not re.sFearch(rule[0]+'/'+'-', text) == None:
                wait = text.replace(rule[0]+'/-', rule[0]+'/'+str(rule[1]))
                path_list_3.append(wait)
            else:
                path_list_3.append(text)
    return path_list_3


if __name__ == "__main__":
    jsons3 = open_n_decode(
        'F:/FrackinUniverse-sChinese-Project/translations/others/dialog/converse.config.patch', "r", "utf_8_sig")
    list233 = [('generic', 70, 1),('cheerful', 31, 1),('jerk', 31, 1),('flirty', 31, 1),('anxious', 31, 1),('easilyspooked',32,1),('clumsy',31,1),('excited',31,1),('intrusive',31,1),('dumb',32,1),('emo',30,1),('fast',31,1),('nocturnal',32,1),('socialite',31,1),('ambitious',30,1)]

    test = trans_patch(jsons3)
    dict_old = dict()
    for i in range(len(test)):
         dict_old['/'+test[i][0]] = test[i][1]
    print(dict_old)
