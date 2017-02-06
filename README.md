### Starbound Frackin' Universe Simplified Chinese Translation Project
* Project：Sky_Orc_Mm
* Credit：TODO

###### 如何帮助翻译？
* 在线编辑。
* 克隆项目至本地，编辑完毕发起 Pull 请求。

###### 查询API
* 此接口用来查询独立翻译进度和未翻译文件，由于GITHUB对未登录用户的API调用频率进行了限制，请登录自己的GITHUB再使用！
* [VZ WEB API](https://zomboid.cn/api/) 

###### 翻译格式
* 翻译源文件为Json格式，Eng表示原文，Chs表示中文。
* 未翻译源文件：
``` json
[
  {
    "DeniedAlternatives": [],
    "Files": {
      "npcs/crew/crewmemberbountyhunter.npctype": [
        "/scriptConfig/dialog/crewmember/offer/default/default/0"
      ]
    },
    "Texts": {
      "Eng": "Hello adventurer, mind if I join you?"
    }
  }
 ```
* 以上为一个未翻译源文件示例。

* 已翻译源文件：
``` json
[
  {
    "DeniedAlternatives": [],
    "Files": {
      "npcs/crew/crewmemberbountyhunter.npctype": [
        "/scriptConfig/dialog/crewmember/offer/default/default/0"
      ]
    },
    "Texts": {
      "Chs": "你好冒险家，介意我加入你们吗？",
      "Eng": "Hello adventurer, mind if I join you?"
    }
  }
 ```
* 以上为一个已翻译源文件示例，遵循Json格式即可。
 
###### 更新周期
* 每周跟进 Frackin' Universe 的最新版本（不含翻译，仅文本跟进更新）。
* ~~目前大量文本尚未完成，尚无准确的编译版本发布时间。~~

###### [2017/2/6|v0.1.8]翻译进度
* 文本量：**8599**
* 已完成：**8343**
* 总进度：**97.02%**

###### 链接信息
* [Steam Workshop](http://steamcommunity.com/sharedfiles/filedetails/?id=754350883)
* [发布版本](https://github.com/ProjectSky/FrackinUniverse-sChinese-Project/releases)

###### 版本备注
* v0.1.8 版本更新（2017/2/6）
