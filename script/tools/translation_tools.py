import os
import os.path
import json
from os import walk, makedirs, remove
from multiprocessing import Pool
import re
from codecs import open
from os.path import dirname, exists, relpath, abspath, basename
from os.path import join as join_path
from sys import platform
from functools import partial
from json_tools import prepare, field_by_path, list_field_paths
from utils import get_answer
import requests
if platform == "win32":
    from os.path import normpath as normpath_old

from dictionary_data import dictionary
from google_trans_new import google_translator


def caiyun_api(source, direction="auto2zh", token="yq7agau781q6ceedn7pn"):
    url = "http://api.interpreter.caiyunai.com/v1/translator"
    # 也许同类产品真没能打的了。
    payload = {
        "source": source,
        "trans_type": direction,
        "request_id": "demo",
        "detect": True,
    }
    headers = {
        'content-type': "application/json",
        'x-authorization': "token " + token,
    }
    response = requests.request(
        "POST", url, data=json.dumps(payload), headers=headers)
    return json.loads(response.text)['target']
# 谷歌翻译，需要用到google_trans_new作依赖。

def google_api(string, lang='zh'):
    translator = google_translator()
    translate_text = translator.translate(
        string, lang_tgt=lang).strip()
    return translate_text


def caiyun_translation(file):
    jsondata = json.loads(prepare(file))
    for i, v in enumerate(jsondata):
        if 'Chs' in jsondata[i]['Texts']:
            pass
        else:
            string_list = jsondata[i]['Texts']['Eng'].splitlines()
            target_list = []
            for string in string_list:
                string = re.sub(re.compile(r'\^.*?\;'), "", string)
                if string.strip() == "":
                    target_list.append(string)
                else:
                    target_list.append(caiyun_api(string))
            target_1 = '\n'.join(target_list)
            jsondata[i]['Texts']['Chs'] = target_1
    result = json.dumps(jsondata, ensure_ascii=False,
                        sort_keys=True, indent=2)
    return result


def google_translation(file):
    jsondata = json.loads(prepare(file))
    for i, v in enumerate(jsondata):
        if 'Chs' in jsondata[i]['Texts']:
            pass
        else:
            string_list = jsondata[i]['Texts']['Eng'].splitlines()
            target_list = list()
            for string in string_list:
                string = re.sub(re.compile(r'\^.*?\;'), "", string)
                if string.strip() == "":
                    target_list.append(string)
                else:
                    target_list.append(google_api(string))
            target_1 = '\n'.join(target_list)
            jsondata[i]['Texts']['Chs'] = target_1
    result = json.dumps(jsondata, ensure_ascii=False,
                        sort_keys=True, indent=2)
    return result


def ge_walk(path, function):
    try:
        for path, d, filelist in os.walk(path):
            for filename in filelist:
                if basename(filename) in ["substitutions.json", "totallabels.json", "translatedlabels.json", "patch_substitutions.json", "parse_problem.txt"]:
                    continue
                i = join_path(path, filename)
                print(basename(i))
                with open(i, "rb+", "utf-8") as f:
                    text = function(f)
                f = open(i, "wb+", "utf-8")
                f.write(text)
                f.close
        print("处理完毕，请仔细校对.")
    except:
        print("无法继续运行，请检查依赖,如request和utils是否已安装，对于翻译，若已安装依赖，则为api欠费")


def replace_from_dictionary(string):
    text = string
    list_to_replace = dictionary.keys()
    for i in list_to_replace:
        text = text.replace(i, dictionary[i])
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


def fix_mark(file):
    jsondata = json.loads(prepare(file))
    fix_1 = re.compile(
        r'([^\^])((?:blue|yellow|red|cyan|green|white|pink|orange|reset|#\w{6});)')
    fix_2 = re.compile(
        r'(\^(?:blue|yellow|red|cyan|green|white|pink|orange|reset|#\w{6}))([^;])')

    for i, v in enumerate(jsondata):
        if 'Chs' in jsondata[i]['Texts']:
            string = jsondata[i]['Texts']['Chs']
            if re.search(fix_1, string) is not None:
                re.sub(fix_1, re.compile(r'$1^$2'), string)
            elif re.search(fix_2, string) is not None:
                re.sub(fix_2, re.compile(r'$1;$2'), string)
            jsondata[i]['Texts']['Chs'] = string
        else:
            pass
    result = json.dumps(jsondata, ensure_ascii=False,
                        sort_keys=True, indent=2)
    return result


def import_patch(patch_dir, file_dir):
    for path, d, filelist in os.walk(file_dir):
        for thefile in filelist:
            if thefile in ["substitutions.json", "totallabels.json", "translatedlabels.json", "patch_substitutions.json", "parse_problem.txt"]:
                continue
            if thefile.endswith(".json"):
                json_file = join_path(path, thefile)
                with open(json_file, "rb+", "utf-8") as f:
                    json_dict = json.load(f)
                    print(basename(json_file))
                for i, v in enumerate(json_dict):
                    for w in json_dict[i]['Files'].keys():
                        patch_file = join_path(patch_dir, w)+".patch"
                        try:
                            patch_data = json.load(
                                open(patch_file, "rb+", "utf-8"))
                        except:
                            continue
                        for y, z in enumerate(patch_data):
                            if json_dict[i]['Files'][w][0] == patch_data[y]["path"]:
                                if patch_data[y]["value"] == json_dict[i]['Texts']['Eng']:
                                    pass
                                else:
                                    json_dict[i]['Texts']['Chs'] = patch_data[y]["value"]
                f = open(json_file, "rb+", "utf-8")
                json.dump(
                    json_dict, f, ensure_ascii=False, indent=2, sort_keys=True)


class Interface:
    handler = None

    def print_info(self):
        print("""
之前写的非常屑的小脚本的集合，界面很拙劣的模仿了龙骑士的写法，确切来说就是复制粘贴。
by diskrubbish
        
1：指定目录以谷歌机翻其中文件
2：指定目录以彩云机翻其中文件
3：指定目录以替换特殊词汇
4：遍历并导入指定patch中的文本
--5：尝试修复指定文件夹中缺失的颜色标记--未完成
-----未完待续？----
0：退出
        """)

    def get_keyword(self, kw):
        if not kw:
            return

        if kw == "1":
            path = input("请输入路径：")
            ge_walk(path, google_translation)
        elif kw == "2":
            path = input("请输入路径：")
            ge_walk(path, caiyun_translation)
        elif kw == "3":
            path = input("请输入路径：")
            ge_walk(path, dict_replace)
        elif kw == "4":
            path1 = input("请输入需要遍历patch的路径：")
            path2 = input("请输入导入文本的路径：")
            import_patch(path1, path2)
        elif kw == "5":
            ##path = input("请输入路径：")
            ##ge_walk(path, fix_mark)
            print("锐意制作中...")
        elif kw == "0":
            exit(1)
        else:
            print("输入的指令不正确！")


if __name__ == '__main__':
    interface = Interface()
    interface.print_info()
    keyword = ""
    while True:
        keyword = input("请输入指令：")
        interface.get_keyword(keyword)
