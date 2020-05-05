# export_mod.py

将extract_labels.py导出的翻译文件转换成patch。

# extract_labels.py

用来导出所有指定文件夹内除patch文件外的可翻译文件。

# extract_patch_labels.py

用来导出所有指定文件夹内patch的可翻译文本，目前基本上没有bug，处理能力有待提升。
更新：2020 5-4 规范了部分代码，增加了识别词条黑名单的能力 by diskrubbish

# ignore_file.py

忽略文件名单，ignore_filelist公用，ignore_filelist_patch只限extract_patch_labels。

# patch_spciallist.py

过滤特殊patch的规则，用于extract_patch_labels。


# parser_settings.py

过滤规则列表。
更新：2020 5-4 修正以前的规则，现在应该不会过滤到界面坐标了;新增增强典键文本的过滤规则 by diskrubbish1

# extract_all_labels.py

很拙略的写了个整合脚本，以后会改的。

# help_translation.py

采用彩云小译的api帮助翻译，并不能代替全部的汉化工作。
更新：2020 5-4 现在能识别英文文本中的颜色符号并去除，方便中文排版 by diskrubbish

# blacklist_patch.py

黑名单，专用于patch文件的过滤

# export_patch.py

导出汉化modpatch中的文本到脚本导出的json种，目前代码很蠢，但是够用