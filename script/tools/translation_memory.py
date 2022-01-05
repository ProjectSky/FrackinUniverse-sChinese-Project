import json
from os import walk
from codecs import open
from os.path import basename, dirname
from os.path import join as join_path
from sys import platform
from json_tools import prepare


def export_memory(root_path, memory_file):
    memory = dict()
    for path, d, filelist in walk(root_path):
        if path.replace(root_path, "").startswith("\others"):
            continue
        for filename in filelist:
            if basename(filename) in ["substitutions.json", "totallabels.json", "translatedlabels.json", "patch_substitutions.json", "parse_problem.txt", "_metadata", "_previewimage", "memory.json"]:
                continue
            i = join_path(path, filename)
            print(basename(i))
            with open(i, "rb+", "utf-8") as f:
                jsondata = json.loads(prepare(f))
                for i, v in enumerate(jsondata):
                    if 'Chs' in jsondata[i]['Texts']:
                        if jsondata[i]['Texts']['Eng'] in memory.keys():
                            pass
                        else:
                            memory[jsondata[i]['Texts']['Eng']
                                   ] = jsondata[i]['Texts']['Chs']
                    else:
                        pass
    result = json.dumps(memory, ensure_ascii=False,
                        sort_keys=True, indent=2)
    f = open(memory_file, "wb+", "utf-8")
    f.write(result)
    f.close


def import_memory(root_path, memory_file):
    memory = json.loads(prepare(open(memory_file, "r", "utf-8")))
    for path, d, filelist in walk(root_path):
        if path.replace(root_path, "").startswith("\others"):
            continue
        for filename in filelist:
            if basename(filename) in ["substitutions.json", "totallabels.json", "translatedlabels.json", "patch_substitutions.json", "parse_problem.txt", "_metadata", "_previewimage", "memory.json"]:
                continue
            i = join_path(path, filename)
            print(basename(i))
            with open(i, "rb+", "utf-8") as f:
                jsondata = json.loads(prepare(f))
                for t, v in enumerate(jsondata):
                    if 'Chs' in jsondata[t]['Texts']:
                        pass
                    else:
                        if jsondata[t]['Texts']['Eng'] in memory.keys():
                            jsondata[t]['Texts']['Chs'] = memory[jsondata[t]
                                                                 ['Texts']['Eng']]
            text = json.dumps(jsondata, ensure_ascii=False,
                              sort_keys=True, indent=2)
            f = open(i, "wb+", "utf-8")
            f.write(text)
            f.close


#export_memory("/git/FrackinUniverse-sChinese-Project/translations","/git/FrackinUniverse-sChinese-Project/memory.json")
#import_memory("/git/FrackinUniverse-sChinese-Project/translations","/git/FrackinUniverse-sChinese-Project/memory.json")
