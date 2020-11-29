import os
import os.path
import json
from dictionary_data import dictionary
from os import walk, makedirs, remove
from multiprocessing import Pool
import re
from codecs import open
from os.path import join, dirname, exists, relpath, abspath, basename
from sys import platform
from json_tools import prepare, field_by_path, list_field_paths
from utils import get_answer
if platform == "win32":
    from os.path import normpath as normpath_old

def replace_from_dictionary(string):
    text = string
    list_to_replace = dictionary.keys()
    for i in list_to_replace:
        text = text.replace(i,dictionary[i])
    return text



def dict_replace(file):
    jsondata = json.loads(prepare(file))
    for i, v in enumerate(jsondata):
        if 'Chs' in jsondata[i]['Texts']:
            pass
        else:
            string = jsondata[i]['Texts']['Eng']
            target_1 = replace_from_dictionary(string)
            jsondata[i]['Texts']['Chs'] = target_1
    result = json.dumps(jsondata, ensure_ascii=False,
                                sort_keys=True, indent=2)
    return result


if __name__ == "__main__":
    print("该脚本可以自动遍历当前输入下的json文件，根据词典替换对应字段。")
    keyword = input("现在，请输入想遍历的目录：")
    for path,d,filelist in os.walk(keyword):
        for filename in filelist:
            i = os.path.join(path,filename)
            print(basename(i))
            with open(i, "rb+", "utf-8") as f:
                text = dict_replace(f)
            f = open(i, "wb+", "utf-8")
            f.write(text)
            f.close
    print("处理完毕，请仔细校对翻译结果！！！！")