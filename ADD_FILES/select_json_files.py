# 作者：微风的龙骑士
# 时间：2018/8/14

# 一个简陋的过滤脚本

# 过滤掉不需要再进行翻译的Json文件，即只删除所有已经翻译完毕的Json文件。
# 传入的参数名应为"Texts"
# 放入translations文件夹下

# 使用方式：依次输入指令1,2,3即可，输入指令0退出。

# 进度：
# + 初步实现
# - 使用json模块进行过滤
# - 提取需要的Chs-Eng键值对，存储到单独的Json文档中，翻译好后，可以逆向替换回去。
# - 可以二次过滤还未翻译完的json文档

import os


class Handler:
    # 默认的Texts路径
    texts_path = ""
    # 已翻译完的文档的路径列表
    translated_json_docs = []
    # 未翻译完的文档的路径列表
    not_translated_json_docs = []

    def __init__(self):
        self.texts_path = os.getcwd()
        if self.texts_path.endswith("ADD_FILES"):
            self.texts_path = self.texts_path.rsplit(
                "\\", 1)[0] + "\\translations\\texts"
        elif self.texts_path.find("FrackinUniverse-Chinese-Project"):
            self.texts_path = self.texts_path + "\\translations" + "\\texts"

        print("当前选定的texts文件夹路径：" + self.texts_path)

    def set_texts_path(self, path: str=None):
        """设置工作路径（即Texts路径）"""
    #     if not path:
    #       self.texts_path = path
        if path:
            self.text_path = path

    def _scan_dir_recursive(self, path):
        """递归扫描指定的目录"""
        # 扫描这个目录，得到所有子目录和子文件实体
        with os.scandir(path) as it:
            entry: os.DirEntry
            # 对于每个实体
            for entry in it:
                # 如果这个实体是文件夹，则保留，并递归调用函数（DirEntry.is_dir()这个方法有问题）
                # 如果没有包含点号则认为是文件夹，这时进行递归调用
                if entry.is_dir and entry.name.find(".") == -1:
                    self._scan_dir_recursive(entry.path)
                # 如果这个实体是文件，则做进一步处理
                else:
                    # 如果是Json文件
                    if entry.name.endswith((".json", ".JSON", ".Json")):
                        self._handle_doc(entry)

    def _handle_doc(self, entry: os.DirEntry):
        """处理（分类）单个文档"""
        # 打开这个文件，指定打开方式和编码
        with open(entry.path, "r", encoding="UTF-8") as f:
            # 通过f.readlines():list(str)得到每一行的文本，并进行遍历
            lines = f.readlines()
            flag = False
            for i in range(len(lines) - 1):
                # 如果某一行定位到Texts属性，且在下一行定位到Eng属性，而非Chs属性
                if lines[i].find(r'"Texts":') != -1 \
                        and lines[i + 1].find(r'"Eng":') != -1:
                    # 标记这个文件为不需要删除的，跳出循环
                    # 其他情况的Json文件都需要标记为要删除的
                    flag = True
                    break
            # 将文档分组
            if not flag:
                self.translated_json_docs.append(entry)
            else:
                self.not_translated_json_docs.append(entry)

    def delete_translated(self):
        """删除已翻译完的文档"""
        for doc in self.translated_json_docs:
            os.remove(doc)
        list.clear(self.translated_json_docs)
        print("删除操作完成！")

    def delete_not_translated(self):
        """删除未翻译的文档"""
        for doc in self.not_translated_json_docs:
            os.remove(doc)
        list.clear(self.not_translated_json_docs)
        print("删除操作完成！")

    def create_markup_files(self):
        """为未翻译完的文件创建markup标记（空文件，.markup后缀）"""
        for doc in self.not_translated_json_docs:
            doc_markup_path = doc.path + ".markup"
            with open(doc_markup_path, "w+"):
                pass

    def delete_markup_files(self):
        for doc in self.not_translated_json_docs:
            mu_path = doc.path + ".markup"
            if os.path.exists(mu_path):
                os.remove(mu_path)
        for doc in self.translated_json_docs:
            mu_path = doc.path + ".markup"
            if os.path.exists(mu_path):
                os.remove(mu_path)

    def print_info(self):
        """打印消息"""
        print("已翻译的Json文件数目：", len(self.translated_json_docs))
        print("未翻译的Json文件数目：", len(self.not_translated_json_docs))


class Interface:
    handler: Handler

    def __init__(self):
        self.handler = Handler()

    def print_info(self):
        """打印消息"""
        print("""
            1：设置路径（Texts，如果就在Texts下，可以忽略）
            2：开始扫描（开始后面的操作前必须先进行扫描）
            3：删除已经翻译完的文档（有危险）
            4：删除未翻译完的文档（有危险）
            5：为未翻译完的文档建立markup文档（空白文档）
            6：删除所有的markup文档（空白文档）
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
            self.handler._scan_dir_recursive(self.handler.texts_path)
            self.handler.print_info()
        elif kw == "3":
            self.handler.delete_translated()
            self.handler.print_info()
        elif kw == "4":
            self.handler.delete_not_translated()
            self.handler.print_info()
        elif kw == "5":
            self.handler.create_markup_files()
        elif kw == "6":
            self.handler.delete_markup_files()
        elif kw == "0":
            exit(1)
        else:
            print("输入的指令不正确！")


if __name__ == '__main__':
    interface = Interface()
    interface.print_info()
    keyword: str
    while True:
        keyword = input("请输入指令：")
        interface.get_keyword(keyword)
