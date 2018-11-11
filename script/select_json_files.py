# 作者：微风的龙骑士
# 时间：2018/8/14

# 一个简陋的过滤脚本
# 区分已翻译完的JSON文件和未翻译完的JSON文件。
# 脚本允许存放在项目根目录、ADD_FILES、translations、script、texts文件夹下。

# 进度：
# DONE：初步实现
# WASTE：使用json模块进行过滤
# DONE：使用os.walk(rootdir)直接扫描到根目录下的所有文件
# TODO：提取需要的Chs-Eng键值对，存储到单独的Json文档中，翻译好后，可以逆向替换回去。
# TODO：可以二次过滤还未翻译完的json文档

# 使用方法：
# 推荐使用VSCode进行协助翻译，加上必要的插件，几乎完美。
# 运行这个脚本，输入指令2，即可得到已翻完和未翻译的Json文件的个数。
# 再次输入指令5，即可为所有未翻译完的文件添空白的.markup文件，标记它们的位置。
# 如果gitignore里面没有加上一行“*.markup”，则所有未翻译完的Json文件的位置都会在资源管理器中以绿色显示。（另外已编辑过的Json文件的位置则会以棕色显示。）
# 这样就可以非常容易地找到有待翻译的文档了。
# 若要提交新翻译的内容，没有必要删除这些标记文件，只需要在gitignore中加上一行“*.markup”。
# 在输入指令2后，输入指令6即可清除所有的markup文件，接着输入指令5更新标记。


import os
import os.path
import json
import re

class Handler:
    # 默认的Texts路径
    texts_path = ""
    # [str]，已翻译完的文档的路径列表（全路径，包括目录、文件名）
    translated_json_list = []
    # [str]，未翻译完的文档的路径列表（全路径，包括目录、文件名）
    not_translated_json_list = []

    # 匹配未翻译文本的字符串（组1：未翻译的英文文本）
    patten = r'"Texts":\s*{\n\s*"Eng":'
    # 对应的Patten对象
    pat = None
    
    def set_texts_path(self, path: str=None):
        """设置工作路径（即Texts路径）"""
        if path:
            self.texts_path = path
   
    def scan_dir(self):
        """遍历扫描指定的目录"""
        for root,dirnames,filenames in os.walk(self.texts_path):
            for filename in filenames:
                #如果是JSON文件
                if str(filename).lower().endswith(".json"):
                    fullpath = os.path.join(root,filename)
                    self._handle_doc(fullpath)
                    
    def _handle_doc(self,fullpath):
        """处理单个文档，进行分组"""   
        # 打开这个文件，指定打开方式和编码
        with open(fullpath, "r", encoding="UTF-8") as f:
            # 读取所有文本
            fd = f.read()
            # 使用re进行匹配，如果result为True，则表明该文档未翻译完，否则翻译完
            # 注意：要在字符串中查找，请用search。match是从字符串开头查找
            result = self.pat.search(fd)
            # 加入分组
            if not result:
                self.translated_json_list.append(fullpath)
            else:    
                self.not_translated_json_list.append(fullpath)
 
    def delete_translated(self):
        """删除已翻译完的文档"""
        for doc in self.translated_json_list:
            os.remove(doc)
        list.clear(self.translated_json_list)
        print("删除操作完成！")

    def delete_not_translated(self):
        """删除未翻译的文档"""
        for doc in self.not_translated_json_list:
            os.remove(doc)
        list.clear(self.not_translated_json_list)
        print("删除操作完成！")

    def create_markup_files(self):
        """为未翻译完的json文档添加标记文件"""
        for doc in self.not_translated_json_list:
            markup_doc = doc + ".markup"
            with open(markup_doc, "w+"):
                pass
        print("创建标记文件完毕！")

    def delete_markup_files(self):
        """删除所有标记文件"""
        # 相对的目录（不包括文件名），最下级目录，文件名
        for root,dirnames,filenames in os.walk(self.texts_path):
            for filename in filenames:
                if str(filename).endswith(".markup"):
                    fullpath = os.path.join(root,filename)
                    os.remove(fullpath)
        print("删除标记文件完毕！")  
        
    def check_json_files(self):
        # 得到translatioins目录
        check_path = self.texts_path.rsplit(os.sep,1)[0]
        flag = True
        for root,dirnames,filenames in os.walk(check_path):
            for filename in filenames:
                if str(filename).lower().endswith((".json",".patch")):
                    with open(os.path.join(root, filename), 'r', encoding='utf-8') as f:
                        try:
                            json.load(f)
                        except ValueError as e:
                            if flag: flag = False 
                            print('错误：' + os.path.join(root, filename) + '\t错误信息：' + str(e))
                            continue
        if flag:
            print("没有发现错误。")   

    def print_info(self):
        """打印消息"""
        print("已翻译的Json文件数目：", len(self.translated_json_list))
        print("未翻译的Json文件数目：", len(self.not_translated_json_list))

    def __init__(self):
        """初始化texts路径，适配多种情况"""
        self.texts_path = os.getcwd()
        if self.texts_path.endswith(("script","ADD_FILES")):
            self.texts_path = self.texts_path.rsplit("\\", 1)[0] + "\\translations\\texts"
        elif self.texts_path.endswith("translations"):
            self.texts_path = self.texts_path + "\\texts"
        elif self.texts_path.find("FrackinUniverse-Chinese-Project") or self.texts_path == "":
            self.texts_path = self.texts_path + "\\translations" + "\\texts"
            
        print("当前选定的texts文件夹路径：" + self.texts_path)
        
        self.pat = re.compile(self.patten)
        

class Interface:
    handler = None

    def print_info(self):
        """打印消息"""
        print("""
区分已翻译完的JSON文件和未翻译完的JSON文件。
脚本允许存放在项目根目录、ADD_FILES、translations、script、texts文件夹下。
        
1：设置路径（*/texts）
2：开始扫描（开始后面的操作前必须先进行扫描）
3：删除已经翻译完的文档（危险）
4：删除未翻译完的文档（危险）
5：为未翻译完的文档建立markup文档（空白文档）
6：删除所有的markup文档（空白文档）
7: 检查所有JSON文件，列出有错误的
0：退出
        """)

    def get_keyword(self, kw):
        """根据指令进行不同的操作"""
        if not kw:
            return

        if kw == "1":
            path = input("请输入路径：")
            self.handler.set_texts_path(path)
        elif kw == "2":
            self.handler.scan_dir()
            self.handler.print_info()
        elif kw == "3":
            if input("请再次确认（Y/N）：").upper() != "Y":
                return      
            self.handler.delete_translated()
            self.handler.print_info()
        elif kw == "4":
            if input("请再次确认（Y/N）：").upper() != "Y":
	            return
            self.handler.delete_not_translated()
            self.handler.print_info()
        elif kw == "5":
            self.handler.create_markup_files()
        elif kw == "6":
            self.handler.delete_markup_files()
        elif kw == "7":
            self.handler.check_json_files()
        elif kw == "0":
            exit(1)
        else:
            print("输入的指令不正确！")
                    
    def __init__(self):
        self.handler = Handler()


if __name__ == '__main__':
    interface = Interface()
    interface.print_info()
    keyword = ""
    while True:
        keyword = input("请输入指令：")
        interface.get_keyword(keyword)