import os
import os.path
import json
from os import walk, makedirs, remove
import re
from codecs import open
from os.path import join, dirname, exists, relpath, abspath, basename
from sys import platform
from json_tools import prepare, field_by_path, list_field_paths
from utils import get_answer
import requests
from patch_tool import trans_patch
if platform == "win32":
    from os.path import normpath as normpath_old


def tanslation(old, new, path):
    w = path
    jsondata = json.loads(prepare(new))
    old_data = old
    dict_old = dict()
    for i in range(len(old_data)):
        dict_old['/'+old_data[i][0]] = old_data[i][1]
    for i, v in enumerate(jsondata):
        if 'Chs' in jsondata[i]['Texts']:
            pass
        else:
            if not w in jsondata[i]['Files']:
                pass
            else:
                for u, v in enumerate(jsondata[i]['Files'][w]):
                    if str(jsondata[i]['Files'][path][u]) in dict_old:
                        jsondata[i]['Texts']['Chs'] = dict_old[str(
                            jsondata[i]['Files'][w][u])]
    result = json.dumps(jsondata, ensure_ascii=False,
                        sort_keys=True, indent=2)
    return result


if __name__ == "__main__":
    print("该脚本可以将patch文件的老文本导入指定json文件，")
    ##old = input("现在，请输入patch文件路径：").replace("\\", "/")
    ##new = input("现在, 请输入json文件夹路径：").replace("\\", "/")
    old = "F:/FrackinRaces-sChinese-Project/release/Fr sChinese"
    new = "F:/FrackinUniverse-sChinese-Project/translations/texts/tech"
    ##old_f = trans_patch(open(old, "r", "utf-8-sig"))
    for path_old, d_old, filelist_old in os.walk(old):
        for filename_old in filelist_old:
            if filename_old.endswith(".patch"):
                w_old = os.path.join(path_old, filename_old)
                path_1 = w_old.replace(old+"\\", "").replace(".patch", "").replace("\\","/")
                print(path_1)
                old_f = trans_patch(open(w_old, "r", "utf-8-sig"))
                for path, d, filelist in os.walk(new):
                    for filename in filelist:
                        if filename.endswith(".json"):
                            w = os.path.join(path, filename)
                            with open(w, "rb+", "utf-8") as f:
                                text = tanslation(old_f, f, path_1)
                            f = open(w, "wb+", "utf-8")
                            f.write(text)
                            f.close
    print("处理完毕。")
