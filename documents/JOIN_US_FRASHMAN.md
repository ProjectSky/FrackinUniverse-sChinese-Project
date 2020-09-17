小白版的协助汉化教程！

Created By 微风的龙骑士 风游迩

Updated By diskrubbish 鸽子

# 建议

推荐的软件：

* VSCode，非常好用的IDE，~~VSC天下第一！~~
* IDEA插件：Starbound Text，提供Starbound富文本的语法高亮和颜色高亮。
* IDEA插件：Translations，提供快捷翻译。
* copytranslator，翻译的利器，偷懒的不二之选。
* capslock+，快速的光标移动、选择以及翻译。

推荐学习：

* Git
* Markdown
* Json

# 加入我们！

~~可能还需要再改改...~~

我已经尽量加得简洁易懂了，可能的确需要再改改...有能的兄贵帮帮我们秋梨膏！

这里以github为例子，码云或者其他地方的网站其实也是大同小异。

接下来，我来手把手一步一步地教各位如何来协助汉化，希望能对有意协助翻译的**小白**有所帮助。

接触过git，vsc的兄贵可以去看龙骑士先辈写的那份。

## 教程正式开始！

### 一、事前准备

1. ~~创建一个Github帐号，并验证邮箱，登陆。（我觉得这个应该不用我说了吧）~~

2. 下载[Git](https://git-scm.com/downloads)，并安装。

3. 创建一个SSH私钥并配置到帐号。篇幅太长，就不在这里写了，参见[LolitaSian大大的教程](https://blog.csdn.net/qq_36667170/article/details/79094257)

4. 返回项目库主页，点击![1QHhHH.png](https://s2.ax1x.com/2020/01/29/1QHhHH.png)，将项目Fork到自己的帐号上。

5. Fork 完成之后，你应该会跳转到Fork下来的项目库页面，请点击![1QLfDU.png](https://s2.ax1x.com/2020/01/29/1QLfDU.png)，在点击如图所示的按钮，复制**克隆项目库需要的链接**，然后粘贴在txt文件里面，后面要用到。![1QxuwT.png](https://s2.ax1x.com/2020/01/29/1QxuwT.png)

6. ~~最好借助文本编辑软件，最好是专门的IDE（我推荐VSCode，因为Atom我更不知道怎样才能使用自如）。~~

VscodeNB！这边强烈推荐使用VSC来进行汉化，去[VScode官网](https://code.visualstudio.com/)，下载安装就可以了。

### 二、开始整活

1. 打开Vscode，~~是不是被满眼e文弄得发慌~~ ，点击左侧的![1QxGlR.png](https://s2.ax1x.com/2020/01/29/1QxGlR.png)搜索并安装以下插件：

   Chinese (Simplified) Language Pack for Visual Studio Code

   GitHub

   Starbound JSON File Syntax

   然后重启Vscode。

2. 接下来，请点击左上角的文件>>打开文件夹，选择你想要存放汉化项目的文件夹。

3. 打开之后，点击终端、新建终端，然后在终端中输入`git clone  克隆项目库需要的链接`，~~记得回车。~~

4. 接下来就是漫长的读条时间，有代理的朋友可以考虑挂代理，方法如下：

   设置代理，在终端中输入：

   ```
   git config --global http.proxy http://你的代理地址
   git config --global https.proxy https://你的代理地址
   ```

   克隆完成后记得取消代理：

   ```
   git config --global --unset http.proxy
   git config --global --unset https.proxy
   ```

5. 克隆完成后，依照上面的方法打开拷贝到本地的项目文件夹。

6. 接下来就可以编辑`translation/texts`和`translation/patch`下的JSON文件了。

   **下面，就是本教程的重头戏。**

   对于JSON文件：

   如果Eng属性上面没对应的Chs属性，如图所示：

   ![1Qxy6I.png](https://s2.ax1x.com/2020/01/30/1Qxy6I.png)

   是这样的话就可以在Eng属性上面加上一行，写成 `"Chs": "翻译后的文本",`，就像这样：![1Qxs1A.png](https://s2.ax1x.com/2020/01/30/1Qxs1A.png)

   如果有的话，也可以视情况修正和润色。

   ***切记！引号和引号后面的冒号和逗号都一定要是英文的嗷！***

7. 然后提交你的汉化成果，点击左侧的![1QxBfH.png](https://s2.ax1x.com/2020/01/30/1QxBfH.png)，在这个侧边栏里面你可以对比查看文件更改前后的差异，确认无误后，点击![1Qxrpd.png](https://s2.ax1x.com/2020/01/30/1Qxrpd.png)>>暂存所有更改>>再点击![1Qx0te.png](https://s2.ax1x.com/2020/01/30/1Qx0te.png)提交~~（叫你输字的时候可以随便输，也可以讲一下你今天干啥）~~，最后点击左下角的![1Qx6Xt.png](https://s2.ax1x.com/2020/01/30/1Qx6Xt.png)进行同步，同步的时候可能会叫你确认github的账号和密码，自己输就是了。

8. 到这一步还不算完。现在，回到你的github项目库主页，点击![1QxL7T.png](https://s2.ax1x.com/2020/01/30/1QxL7T.png)，跳转之后再点击![1QxgnP.png](https://s2.ax1x.com/2020/01/30/1QxgnP.png)，输入标题之后，创建请求，你的第一次协助就完成了。~~（至于解决冲突？快去百度学习啊kora！）~~~

# 一些需要注意的地方：

* **再说一遍！引号和引号后面的冒号和逗号都一定要是英文的嗷！**
* 对于 `前面^red; 中间^reset;后面` 一类的文本，把其看成`前面中间后面`拿出来翻译，翻译完一定要在相应的地方插入两端的**颜色识别符**
* 善加利用全局搜索（Ctrl+Shift+F）和全局替换（Ctrl+Shift+H）。
* 特殊名词请参考`REFERENCE.md`和 `TEMPLATE.md`这两个文档。
* 如果使用Windows系统，由于对文件的大小写不敏感，源代码管理中的更改一栏下面，可能会存在一些怎么也提交不了的含有大写字母的文档。忽略即可。
* 文本中换行符太多了，眼花看不清怎么办：如果你使用的是IDEA并且安装了Starbound Text插件的话，可以将鼠标移到文本上，输入Alt+Enter，然后选择"Edit Starbound Text Fragment"，在临时窗口中编辑文本。

