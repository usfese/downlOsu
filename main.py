from tkinter import *
from tkinter.ttk import *

from config_helper import *
from info import PROJECT_NAME, PROJECT_VERSION


# 窗口初始化函数
def window_init(window):
    window.title(PROJECT_NAME + " " + PROJECT_VERSION)
    window.geometry("500x400")


# 读取配置

# 主逻辑
if __name__ == '__main__':
    # 窗口初始化
    window = Tk()
    window_init(window)
    # 初始化配置
    config = read_config_from_file()
    if config == None:
        try_init_config()

    # Songs文件夹路径设置
    # 分类标签
    label_type = Label(window, text="分类：")
    label_type.grid(column=0, row=0)
    # 分类输入
    type_selected = IntVar()
    type1 = Radiobutton(window, text="hot", value=1, variable=type_selected)
    type1.grid(column=1, row=0)
    type2 = Radiobutton(window, text="new", value=2, variable=type_selected)
    type2.grid(column=2, row=0)
    type3 = Radiobutton(window, text="pack", value=3, variable=type_selected)
    type3.grid(column=3, row=0)
    type4 = Radiobutton(window, text="search", value=4, variable=type_selected)
    type4.grid(column=4, row=0)
    # 搜索关键字标签
    label_keyword = Label(window, text="搜索关键字：")
    label_keyword.grid(column=0, row=1)
    # 搜索关键字输入
    keyword_entered = StringVar()
    entry_keyword = Entry(window, width=30)
    entry_keyword.grid(column=1, row=1)
    # 精确匹配标签
    label_subType = Label(window, text="精确匹配：")
    label_subType.grid(column=0, row=2)
    # 精确匹配输入
    subType_selected = IntVar()
    subType1 = Radiobutton(window, text="title/titleU", value=1, variable=subType_selected)
    subType1.grid(column=1, row=2)
    subType2 = Radiobutton(window, text="artist/artistU", value=2, variable=subType_selected)
    subType2.grid(column=2, row=2)
    subType3 = Radiobutton(window, text="creator", value=4, variable=subType_selected)
    subType3.grid(column=3, row=2)
    subType4 = Radiobutton(window, text="version", value=8, variable=subType_selected)
    subType4.grid(column=4, row=2)
    subType5 = Radiobutton(window, text="tags", value=16, variable=subType_selected)
    subType5.grid(column=5, row=2)
    subType6 = Radiobutton(window, text="source", value=32, variable=subType_selected)
    subType6.grid(column=6, row=2)

    # 主循环
    window.mainloop()
