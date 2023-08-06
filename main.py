from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

from config_helper import *
from info import PROJECT_NAME, PROJECT_VERSION


# 窗口初始化函数
def window_init(window):
    window.title(PROJECT_NAME + " " + PROJECT_VERSION)
    window.geometry("700x400")
    window.resizable(0, 0)


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
        config = read_config_from_file()

    # Songs文件夹路径设置
    # 路径标签
    label_songs = Label(window, text="Songs文件夹路径：")
    label_songs.grid(row=0, column=0, sticky="w", padx="3px")
    songs_dir = StringVar()
    songs_dir.set(config["songsDir"])
    entry_songs = Entry(window, textvariable=songs_dir, state="readonly", width=50)
    entry_songs.grid(row=0, column=1, columnspan=4)


    # 路径输入
    # 定义处理函数
    def on_button_click():
        dir = filedialog.askdirectory()
        if dir != "":
            config["songsDir"] = dir
            write_config(config)
            songs_dir.set(config["songsDir"])


    button_songs_dir = Button(window, text="...", command=on_button_click)
    button_songs_dir.grid(row=0, column=5, sticky="w")
    # 分类标签
    label_type = Label(window, text="分类：")
    label_type.grid(column=0, row=2, sticky="w", padx="3px")
    # 数量标签
    label_num = Label(window, text="下谱数量(0~1000)")
    label_num.grid(row=1, column=0, sticky="w", padx="3px")
    # 数量输入
    num_str = StringVar()
    num_str.set("10")
    num_entered = Spinbox(window, from_=0, to=1000, increment=1, textvariable=num_str)
    num_entered.grid(row=1, column=1, columnspan=2)
    # 分类输入
    type_selected = IntVar()
    type1 = Radiobutton(window, text="hot", value=1, variable=type_selected)
    type1.grid(row=2, column=1)
    type2 = Radiobutton(window, text="new", value=2, variable=type_selected)
    type2.grid(row=2, column=2)
    type3 = Radiobutton(window, text="pack", value=3, variable=type_selected)
    type3.grid(row=2, column=3)
    type4 = Radiobutton(window, text="search", value=4, variable=type_selected)
    type4.grid(row=2, column=4)
    # 搜索关键字标签
    label_keyword = Label(window, text="搜索关键字：")
    label_keyword.grid(column=0, row=2, sticky="w", padx="3px")
    # 搜索关键字输入
    keyword_entered = StringVar()
    entry_keyword = Entry(window, width=60)
    entry_keyword.grid(column=1, row=2, columnspan=5, pady="3px")
    # 精确匹配标签
    label_subType = Label(window, text="精确匹配：")
    label_subType.grid(column=0, row=3, sticky="w", padx="3px")
    # 精确匹配输入
    subType_selected = IntVar()
    subType1 = Radiobutton(window, text="title/titleU", value=1, variable=subType_selected)
    subType1.grid(column=1, row=3)
    subType2 = Radiobutton(window, text="artist/artistU", value=2, variable=subType_selected)
    subType2.grid(column=2, row=3)
    subType3 = Radiobutton(window, text="creator", value=4, variable=subType_selected)
    subType3.grid(column=3, row=3)
    subType4 = Radiobutton(window, text="version", value=8, variable=subType_selected)
    subType4.grid(column=4, row=3)
    subType5 = Radiobutton(window, text="tags", value=16, variable=subType_selected)
    subType5.grid(column=5, row=3)
    subType6 = Radiobutton(window, text="source", value=32, variable=subType_selected)
    subType6.grid(column=6, row=3)
    # 模式标签
    label_mode = Label(window, text="模式:")
    label_mode.grid(row=4, column=0, sticky="w", padx="3px")
    # 模式输入
    mode_selected = IntVar()
    mode1 = Radiobutton(window, text="std", value=1, variable=mode_selected)
    mode1.grid(row=4, column=1)
    mode2 = Radiobutton(window, text="taiko", value=2, variable=mode_selected)
    mode2.grid(row=4, column=2)
    mode3 = Radiobutton(window, text="ctb", value=4, variable=mode_selected)
    mode3.grid(row=4, column=3)
    mode4 = Radiobutton(window, text="mania", value=8, variable=mode_selected)
    mode4.grid(row=4, column=4)
    # 谱面状态标签
    label_class = Label(window, text="谱面状态:")
    label_class.grid(row=5, column=0, sticky="w", padx="3px")
    # 谱面状态输入
    class_selected = IntVar()
    class1 = Radiobutton(window, text="Ranked & Approved", value=1, variable=class_selected)
    class1.grid(row=5, column=1)
    class2 = Radiobutton(window, text="Qualified", value=2, variable=class_selected)
    class2.grid(row=5, column=2)
    class3 = Radiobutton(window, text="Loved", value=4, variable=class_selected)
    class3.grid(row=5, column=3)
    class4 = Radiobutton(window, text="Pending & WIP", value=8, variable=class_selected)
    class4.grid(row=5, column=4)
    class5 = Radiobutton(window, text="Graveyard", value=16, variable=class_selected)
    class5.grid(row=5, column=5)
    # stars标签
    label_stars = Label(window, text="stars范围(0~20):")
    label_stars.grid(row=6, column=0, sticky="w", padx="3px")
    # stars输入
    stars_from_str = StringVar()
    stars_from_str.set("0.0")
    stars_from = Spinbox(window, from_=0.0, to=20.0, width=10, increment=0.1, textvariable=stars_from_str)
    stars_from.grid(row=6, column=1)
    stars_to_str = StringVar()
    stars_to_str.set("20.0")
    stars_to = Spinbox(window, from_=0.0, to=20.0, width=10, increment=0.1, textvariable=stars_from_str)
    stars_to.grid(row=6, column=2)
    # ar标签
    label_ar = Label(window, text="ar范围(0~10):")
    label_ar.grid(row=7, column=0, sticky="w", padx="3px")
    # ar输入
    ar_from_str = StringVar()
    ar_from_str.set("0.0")
    ar_from = Spinbox(window, from_=0.0, to=10.0, width=10, increment=0.1, textvariable=ar_from_str)
    ar_from.grid(row=7, column=1)
    ar_to_str = StringVar()
    ar_to_str.set("10.0")
    ar_to = Spinbox(window, from_=0.0, to=10.0, width=10, increment=0.1, textvariable=ar_from_str)
    ar_to.grid(row=7, column=2)
    # od标签
    label_od = Label(window, text="od范围(0~10):")
    label_od.grid(row=8, column=0, sticky="w", padx="3px")
    # od输入
    od_from_str = StringVar()
    od_from_str.set("0.0")
    od_from = Spinbox(window, from_=0.0, to=10.0, width=10, increment=0.1, textvariable=od_from_str)
    od_from.grid(row=8, column=1)
    od_to_str = StringVar()
    od_to_str.set("10.0")
    od_to = Spinbox(window, from_=0.0, to=10.0, width=10, increment=0.1, textvariable=od_from_str)
    od_to.grid(row=8, column=2)
    # cs标签
    label_cs = Label(window, text="cs范围(0~10):")
    label_cs.grid(row=9, column=0, sticky="w", padx="3px")
    # cs输入
    cs_from_str = StringVar()
    cs_from_str.set("0.0")
    cs_from = Spinbox(window, from_=0.0, to=10.0, width=10, increment=0.1, textvariable=cs_from_str)
    cs_from.grid(row=9, column=1)
    cs_to_str = StringVar()
    cs_to_str.set("10.0")
    cs_to = Spinbox(window, from_=0.0, to=10.0, width=10, increment=0.1, textvariable=cs_from_str)
    cs_to.grid(row=9, column=2)
    # length标签
    label_length = Label(window, text="length范围(0~1000):")
    label_length.grid(row=10, column=0, sticky="w", padx="3px")
    # length输入
    length_from_str = StringVar()
    length_from_str.set("0")
    length_from = Spinbox(window, from_=0, to=1000, width=10, increment=1, textvariable=length_from_str)
    length_from.grid(row=10, column=1)
    length_to_str = StringVar()
    length_to_str.set("1000")
    length_to = Spinbox(window, from_=0, to=1000, width=10, increment=1, textvariable=length_from_str)
    length_to.grid(row=10, column=2)
    # bpm标签
    bpm_length = Label(window, text="bpm范围(0~1000):")
    bpm_length.grid(row=11, column=0, sticky="w", padx="3px")
    # length输入
    bpm_from_str = StringVar()
    bpm_from_str.set("0")
    bpm_from = Spinbox(window, from_=0, to=1000, width=10, increment=1, textvariable=bpm_from_str)
    bpm_from.grid(row=11, column=1)
    bpm_to_str = StringVar()
    bpm_to_str.set("1000")
    bpm_to = Spinbox(window, from_=0, to=1000, width=10, increment=1, textvariable=bpm_from_str)
    bpm_to.grid(row=11, column=2)

    # 主循环
    window.mainloop()
