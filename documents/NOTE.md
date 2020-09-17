修复缺失分号的颜色标记：

```
(\^(?:blue|yellow|red|cyan|green|white|pink|orange|#\w{6}))([^;])
->
$1;$2
```