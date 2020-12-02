import os
import os.path
import json
from os import walk, makedirs, remove
import re
from codecs import open
from os.path import join, dirname, exists, relpath, abspath, basename, isfile
from sys import platform
from json_tools import prepare, field_by_path, list_field_paths
from utils import get_answer

from patch_tool import trans_patch
if platform == "win32":
    from os.path import normpath as normpath_old


def import_patch(patch_dir, file_dir):
    for path, d, filelist in os.walk(file_dir):
        for thefile in filelist:
            if thefile in ["substitutions.json", "totallabels.json", "translatedlabels.json", "patch_substitutions.json", "parse_problem.txt"]:
                continue
            if thefile.endswith(".json"):
                json_file = join(path, thefile)
                with open(json_file, "rb+", "utf-8") as f:
                    json_dict = json.load(f)
                    print(basename(json_file))
                for i, v in enumerate(json_dict):
                    for w in json_dict[i]['Files'].keys():
                        patch_file = join(patch_dir, w)+".patch"
                        try:
                            patch_data = json.load(
                                open(patch_file, "rb+", "utf-8"))
                        except:
                            continue
                        for y, z in enumerate(patch_data):
                            if json_dict[i]['Files'][w][0] == patch_data[y]["path"]:
                                json_dict[i]['Texts']['Chs'] = patch_data[y]["value"]
                f = open(json_file, "rb+", "utf-8")
                json.dump(
                    json_dict, f, ensure_ascii=False, indent=2, sort_keys=True)


if __name__ == "__main__":
    patch_dir_1 = "F:/Pandoras-Box_sChinese_Project/mods"
    file_dir_1 = "F:/FrackinUniverse-sChinese-Project/translations/texts/interface"
    import_patch(patch_dir_1, file_dir_1)
