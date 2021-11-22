加入我们！

Created By 微风的龙骑士 风游迩

# 建议

推荐的软件：

* VSCode，非常好用的IDE。
* IDEA，更加强大的IDE。
* IDEA插件：Starbound Text，提供Starbound富文本的语法高亮和颜色高亮。
* IDEA插件：Translations，提供快捷翻译。
* capslock+，快速的光标移动、选择以及翻译。

推荐学习：

* Git
* Markdown
* Json

# 翻译步骤

说一下翻译步骤，希望能对有意协助翻译的人有所帮助。

1. 创建一个Github帐号，并验证邮箱。
2. 创建一个SSH私钥并配置到帐号。
3. 访问项目地址，申请成为协作者。
4. Fork整个项目到自己的帐号，或者本地（下载压缩包）。

有了权限，接下来就可以协助进行翻译了。

最好借助文本编辑软件，最好是专门的IDE（IDEA天下第一！）。

5. 使用IDE打开拷贝到本地的项目。
6. 从FAST分支新建一个属于自己的分支（签出）。
7. 在该分支下，开始编辑`translation/texts`文件夹下面的JSON文件。
8. 如果Eng属性上面没对应的Chs属性，就可以加上一行，写成 `"Chs": "翻译后的文本",`的格式。如果已有，也可以视情况修正和润色。
9. 翻译了一定进度后，就可以通过提交（Commit）- 推送（Push），同步更改到远程的你的分支。
10. 确认无误后，就可以通过拉取自（Pull From） - 远程分支FAST（Origin/FAST），将FAST分支中的更改拉到自己的分支里面。
11. 解决完合并冲突之后，就可以申请合并分支了。在项目网页 - 自己的分支那里点击“提交合并请求”即可。

一些需要注意的地方：

* 使用 ^red; 设置文本颜色， ^reset; 重置颜色。
* 善加利用全局搜索（Ctrl+Shift+F）和全局替换（Ctrl+Shift+H）。
* 特殊名词请参考`REFERENCE.md`和 `TEMPLATE.md`这两个文档。
* 如果使用Windows系统，由于对文件的大小写不敏感，源代码管理中的更改一栏下面，可能会存在一些怎么也提交不了的含有大写字母的文档。忽略即可。

starbound富文本的语法支持：

* 如果你使用是IDEA IDE的话，你可以通过安装Starbound Text插件来提供Starbound富文本的语言支持。
* 要想永久性将translations/texts目录下的json文件中的Chs属性的值识别为Starbound富文本，你需要绑定json schema文件与该目录下的所有json文件。打开任意json文件，点击右下角的“Schema...”，点击“Edit Schema Mapping”，添加目录类型的Schema Mapping，选择项目目录下的schema/text.yml作为schema文件，选择项目目录下的translations/texts作为要绑定的目录，即可完成绑定。
* 成功绑定后，打开translation/texts目录下的任意json文件，等待完成文件结构解析后，你应当看到其中的Chs属性的值有了颜色标记的高亮，但Eng属性不做识别。
* 可以将鼠标移到文本上，输入Alt+Enter，然后选择"Edit Starbound Text Fragment"，在临时窗口中更直观地编辑文本。（**注意：存在bug，谨慎使用！**）
* 这会高亮文本为对应的颜色（包括#fff格式的自定义颜色），将换行符“\n”替换成真正的换行，并可通过collapse all折叠所有颜色标记，将颜色标记统一折叠为“<>”，提供更好的预览效果。
* 如果存在语法解析的错误，IDEA的编辑器中会报错，也可通过Inspect Code检查代码功能，将项目中的所有语法解析错误列出来。
* 注意IDEA在编辑临时窗口中的文本时，折叠颜色标记后，可能会有自身的bug，没有将临时窗口中的文本完全同步到原本的json文件中。
