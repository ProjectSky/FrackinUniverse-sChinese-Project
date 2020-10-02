在文档中查找未翻译的文本的正则表达式：

```
"Texts":\s*\{\n\s*"Eng":
```

为未翻译的文本添加不加改动的翻译文本：

```
"Texts": \{\n      "Eng": "(.*)"
-->
"Texts": {\n      "Chs": "$1",\n      "Eng": "$1"
```

修复缺失分号的颜色标记：

```
(\^(?:blue|yellow|red|cyan|green|white|pink|orange|#\w{6}))([^;])
->
$1;$2
```

`\ue024`：不知道是啥unicode，显示不出来
