import os
import os.path
import json
from os import walk, makedirs, remove
from multiprocessing import Pool
import re
from codecs import open
from os.path import join, dirname, exists, relpath, abspath, basename
from sys import platform
from json_tools import prepare, field_by_path, list_field_paths
from utils import get_answer
import requests
if platform == "win32":
    from os.path import normpath as normpath_old


class Interface:
    handler = None

## 采用了彩云小译的api
def tranlate(source, direction):
    url = "http://api.interpreter.caiyunai.com/v1/translator"
    # WARNING, this token is a test token for new developers, and it should be replaced by your token
    token = "yq7agau781q6ceedn7pn"
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

#添加了自动删除颜色标识的功能！
def tanslation(file):
    jsondata = json.loads(prepare(file))
    for i, v in enumerate(jsondata):
        if 'Chs' in jsondata[i]['Texts']:
            pass
        else:
            string = re.sub(re.compile(r'\^.*?\;'),"",jsondata[i]['Texts']['Eng'])
            #string = jsondata[i]['Texts']['Eng']
            target_1 = tranlate(string, "auto2zh")
            jsondata[i]['Texts']['Chs'] = target_1
    result = json.dumps(jsondata, ensure_ascii=False,
                                sort_keys=True, indent=2)
    return result


if __name__ == "__main__":
    print("该脚本可以自动遍历当前输入下的json文件，且利用api自动添加翻译，但不保证翻译结果准确！")
    keyword = input("现在，请输入想遍历的目录：")
    for path,d,filelist in os.walk(keyword):
        for filename in filelist:
            i = os.path.join(path,filename)
            print(basename(i))
            with open(i, "rb+", "utf-8") as f:
                text = tanslation(f)
            f = open(i, "wb+", "utf-8")
            f.write(text)
            f.close
    print("处理完毕，请仔细校对翻译结果！！！！")