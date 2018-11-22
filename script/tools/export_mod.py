#!/usr/bin/python3

from os import walk, makedirs, sep
from os.path import join, relpath, dirname, exists, normpath, basename
from json import load, dump
from shutil import copy
from json_tools import field_by_path
from re import compile as regex
from codecs import open as copen
import configparser


def uopen(path, mode):
    return copen(path, mode, "utf-8")


translations_dir = "FrackinUniverse-sChinese-Project/translations"
mod_dir = "mods"

checker = regex('([^\n\s\t\r]+|\r?[\n\s\t])')
is_unprintable = regex('\^.+;')

patchfiles = dict()

emotes = dict()
glitchFixed = list()
labelsTotal = dict()
labelsTranslated = dict()

others_path = normpath(join(translations_dir, "others"))
others_dest = normpath(mod_dir)


def sum_up_counter(counter):
    result = 0
    for l, n in counter.items():
        if not type(n) is int:
            result += sum_up_counter(n)
        else:
            result += n
    return result


def set_count(counter, path, value):
    thepath = normpath(relpath(path, translations_dir))
    field_by_path(counter, thepath, value, sep)


def add_count(counter, path, value):
    thepath = normpath(relpath(path, translations_dir))
    oldval = field_by_path(counter, thepath, sep=sep)
    field_by_path(counter, thepath, oldval + 1, sep)


def check_translation_length(text):
    # 15 height, 36 width
    words = checker.split(text)
    maxwidth = 40
    width = maxwidth
    height = 17 - 1
    for word in words:
        wlen = len(word)
        if wlen == 0 or is_unprintable.match(word):
            continue
        if word == '\n':
            height -= 1
            width = maxwidth
            continue
        width -= wlen
        if width < 0 and not word == ' ':
            width = maxwidth - wlen
            height -= 1
    return height >= 0


specials = dict()

for subdir, dirs, files in walk(translations_dir):
    for thefile in files:
        if thefile in ["substitutions.json", "totallabels.json", "translatedlabels.json"]:
            continue
        filename = normpath(join(subdir, thefile))
        if filename.startswith(others_path):
            filename = relpath(filename, others_path)
            dest = join(others_dest, filename)
            makedirs(dirname(dest), exist_ok=True)
            copy(join(subdir, thefile), dest)
            continue
        filename = normpath(join(subdir, thefile))
        jsondata = list()
        try:
            with uopen(filename, "r") as f:
                jsondata = load(f)
        except:
            print("Cannot parse file: " + filename)
            continue
        set_count(labelsTotal, filename, len(jsondata))
        set_count(labelsTranslated, filename, 0)
        for label in jsondata:
            if "Chs" not in label["Texts"] or len(label["Texts"]["Chs"]) == 0:
                continue

            add_count(labelsTranslated, filename, 1)
            translation = label["Texts"]["Chs"]
            if filename.endswith("codex.json") and not check_translation_length(translation):
                print("Warning! String too long in file: " + filename)

            for originfile, jsonpaths in label["Files"].items():
                patchfile = normpath(join(mod_dir, originfile + ".patch"))
                if patchfile not in patchfiles:
                    patchfiles[patchfile] = list()
                for jsonpath in jsonpaths:
                    specialpaths = ["glitchEmote", "glitchEmotedText"]
                    jsonpathend = basename(jsonpath)
                    if jsonpathend in specialpaths:
                        if patchfile not in specials:
                            specials[patchfile] = dict()
                        specials[patchfile][jsonpath] = translation
                        specialpaths.remove(jsonpathend)
                        basepath = dirname(jsonpath)
                        restpath = join(basepath, specialpaths.pop())
                        if restpath in specials[patchfile]:
                            emotepath = join(basepath, "glitchEmote")
                            textpath = join(basepath, "glitchEmotedText")
                            emote = specials[patchfile][emotepath]
                            text = specials[patchfile][textpath]
                            command = dict()
                            command["op"] = "replace"
                            command["value"] = emote + " " + text
                            command["path"] = basepath
                            patchfiles[patchfile].append(command)
                    else:
                        command = dict()
                        command["op"] = "replace"
                        command["value"] = translation
                        command["path"] = jsonpath
                        patchfiles[patchfile].append(command)

for pfile, content in patchfiles.items():
    makedirs(dirname(pfile), exist_ok=True)
    thecontent = content
    if exists(pfile):
        with uopen(pfile, 'r') as f:
            thecontent += load(f)
    with uopen(pfile, "w") as f:
        dump(thecontent, f, ensure_ascii=False, indent=2)

labelsTranslatedN = 0
labelsTotalN = 0

labelsTotalN = sum_up_counter(labelsTotal)
labelsTranslatedN = sum_up_counter(labelsTranslated)

with uopen(join(translations_dir, "translatedlabels.json"), "w") as f:
    dump(labelsTranslated, f, indent=2, sort_keys=True)
with uopen(join(translations_dir, "totallabels.json"), "w") as f:
    dump(labelsTotal, f, indent=2, sort_keys=True)

'''
pex = '/home/sky/script/main/'
config = configparser.ConfigParser()
config.read(pex + "config/config.ini")

def writeConfig():
  #config.add_section("progress")
  config.set("progress",'labelsTranslatedN',str(labelsTranslatedN))
  config.set("progress",'labelsTotalN',str(labelsTotalN))
  config.set("progress",'completion',str(labelsTranslatedN*100/labelsTotalN))
  with open(pex + 'config/config.ini', 'w') as f:
    config.write(f)
    
writeConfig()

f = open("/home/sky/script/main/config/progress.txt","w")
f.write("[list]")
f.write("\n[*] 已翻译: " + str(labelsTranslatedN))
f.write("\n[*] 文本量: " + str(labelsTotalN))
f.write("\n[*] 总进度: " + str(labelsTranslatedN*100/labelsTotalN) + "%")
f.write("\n[/list]")
f.close()
'''
