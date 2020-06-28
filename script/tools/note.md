# export_mod.py

将extract_labels.py导出的翻译文件转换成patch。

# extract_labels.py

用来导出所有指定文件夹内的可翻译文件。

2020 6-28 已与extract_labels_patch.py合并为一个脚本，优化了各处的代码，将配置变量独立到extract_labels_config.py。

# extract_labels_config.py

extract_labels.py的可配置参数。

# ~~extract_patch_labels.py~~

~~用来导出所有指定文件夹内patch的可翻译文本，目前基本上没有bug，处理能力有待提升。~~
~~更新：2020 5-4 规范了部分代码，增加了识别词条黑名单的能力 by diskrubbish~~

2020 6-28 已与extract_labels.py合并为一个脚本。  by diskrubbish

# ignore_file.py

忽略文件名单。

# patch_spciallist.py

过滤特殊patch的规则。


# parser_settings.py

过滤规则列表。
更新：2020 5-4 修正以前的规则，现在应该不会过滤到界面坐标了;新增增强典籍文本的过滤规则 by diskrubbish
    2020 5-14 添加 spaceStationData.config 的有关规则  by diskrubbish

# ~~extract_all_labels.py~~

~~很拙略的写了个整合脚本，以后会改的。~~ 已经弃置

# help_translation.py

采用彩云小译的api帮助翻译，并不能代替全部的汉化工作。
更新：2020 5-4 现在能识别英文文本中的颜色符号并去除，方便中文排版 by diskrubbish

# blacklist.py

过滤黑名单，包含目录黑名单和path黑名单。

# ~~blacklist_patch.py~~

~~黑名单，专用于patch文件的过滤~~ 已经弃置

# export_patch.py

导出汉化mod的patch中的文本到脚本导出的json中，目前代码比较蠢，够用了，以后再修

# armor_dictionary.py

尝试自动翻译盔甲效果的产物，目前搁置。

