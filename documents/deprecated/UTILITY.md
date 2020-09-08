	Created By 微风的龙骑士 风游迩  
	实用工具收集（正则表达式、关键词等）

# 有用的正则表达式

在文档中查找未翻译的文本的正则表达式：  
`"Texts":\s*{\n\s*"Eng":`

为未翻译的文本添加不加改动的翻译文本：
`"Texts": {\n      "Eng": "(.*)"`  
-->`"Texts": {\n      "Chs": "$1",\n      "Eng": "$1"`

# 颜色参考

```css
* {
	color: cyan;		/*通用正面效果*/
	color: green;		/*附加效果，描述性的效果*/
	color: yellow;		/*武器特性*/
	color: red;			/*通用负面效果*/
	
	color: #c74eff;		/*条件效果：武器*/
	color: #e43774;		/*条件效果：生态*/
	
	color: orange;		/*突出显示的数值或范围*/
} 
```
