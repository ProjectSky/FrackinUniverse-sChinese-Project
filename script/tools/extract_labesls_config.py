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
##设定文本源和目标文件夹
texts_prefix = "texts"
sub_file = normpath(join(prefix, "substitutions.json"))
patch_texts_prefix = "patches"
patch_sub_file = normpath(join(prefix, "patch_substitutions.json"))
##有关patch文件文件夹的设定
error_list_file = normpath(join(prefix, "parse_problem.txt"))
#过滤失败文件名单文件名设置
parse_process_number = 8
#过滤进程数设定，默认为8