# export_mod.py

将extract_labels.py导出的翻译文件转换成patch。

2020 11-29 现在当中文与英文相同时，pass。

# extract_labels.py

用来导出所有指定文件夹内的可翻译文件。

2020 6-28 已与extract_labels_patch.py合并为一个脚本，优化了各处的代码，将配置变量独立到extract_labels_config.py。

2020 11-29 优化了过滤patch的逻辑，更加丝滑更加强大（不是）

# extract_labels_config.py

extract_labels.py的可配置参数。
2020 11-29 将patch_spciallist.py并入其中

# ~~extract_patch_labels.py~~

~~用来导出所有指定文件夹内patch的可翻译文本，目前基本上没有bug，处理能力有待提升。~~
~~更新：2020 5-4 规范了部分代码，增加了识别词条黑名单的能力 by diskrubbish~~

2020 6-28 已与extract_labels.py合并为一个脚本。  by diskrubbish

# ignore_file.py

忽略文件名单。

# ~~patch_spciallist.py~~

~~过滤特殊patch的规则。~~

2020 11-29 已并入extract_labels_config。


# parser_settings.py

过滤规则列表。
更新：2020 5-4 修正以前的规则，现在应该不会过滤到界面坐标了;新增增强典籍文本的过滤规则 by diskrubbish
    2020 5-14 添加 spaceStationData.config 的有关规则  by diskrubbish

# ~~extract_all_labels.py~~

~~很拙略的写了个整合脚本，以后会改的。~~ ~~已经弃置~~ 已经删除

# ~~help_translation.py~~

~~采用彩云小译的api帮助翻译，并不能代替全部的汉化工作。~~

~~api用我自己的，所以能不能用要看我钱包啦。（~~

~~更新：2020 5-4 现在能识别英文文本中的颜色符号并去除，方便中文排版 by diskrubbish~~

目前已加入translation_tools.py中

# blacklist.py

过滤黑名单，包含目录黑名单和path黑名单。

# ~~blacklist_patch.py~~

~~黑名单，专用于patch文件的过滤~~ 已经弃置

# ~~export_patch.py~~

~~导出汉化mod的patch中的文本到脚本导出的json中，目前代码还好，比以前智能力，，~~

目前已加入translation_tools.py中

# ~~dict_replace.py~~

对于特殊词汇的不靠谱的替换PY，~~目前搁置~~目前已加入translation_tools.py中

# translation_tools.py

help_translation、dict_replace、export_patch三个脚本的合集，复制粘贴的屑作。

未来大概还会增加新的功能？大概吧，鸽了。

