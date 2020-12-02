from os.path import abspath, basename, dirname, exists, join, relpath
from sys import platform
if platform == "win32":
    from os.path import normpath as normpath_old

    def normpath(path):
        return normpath_old(path).replace('\\', '/')
else:
    from os.path import normpath
root_dir = "/FrackinUniverse/"
prefix = "/FrackinUniverse-sChinese-Project/translations/"
# 设定文本源和目标文件夹
texts_prefix = "texts"
sub_file = normpath(join(prefix, "substitutions.json"))
patch_texts_prefix = "patches"
patch_sub_file = normpath(join(prefix, "patch_substitutions.json"))
# 有关patch文件文件夹的设定
error_list_file = normpath(join(prefix, "parse_problem.txt"))
# 过滤失败文件名单文件名设置
parse_process_number = 8
# 过滤进程数设定，默认为8
patch_serialization = {
    "craftingmedical.object.patch": [('upgradeStages', 2, 0)],
    "statuses.config.patch": [('generic', 70, 1), ('cheerful', 31, 1), ('jerk', 31, 1), ('flirty', 31, 1), ('anxious', 31, 1), ('easilyspooked', 32, 1), ('clumsy', 31, 1), ('excited', 31, 1), ('intrusive', 31, 1), ('dumb', 32, 1), ('emo', 30, 1), ('fast', 31, 1), ('nocturnal', 32, 1), ('socialite', 31, 1), ('ambitious', 30, 1)],
    'craftingfurnace.object.patch': [('upgradeStages', 3, 0)],
    'craftingwheel.object.patch': [('upgradeStages', 2, 0)]
}
#针对某些path中的-的替换规则
