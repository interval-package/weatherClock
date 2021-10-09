from pageFrames import *
import threading as thd

class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.clockPage = clockPage(self.root)  # 创建不同Frame
        self.weatherPage = weatherPage(self.root)
        self.clockPage.pack()  # 默认显示数据录入界面
        menubar = Menu(self.root)
        menubar.add_command(label='时钟', command=self.clockShow)
        menubar.add_command(label='天气', command=self.weatherShow)
        self.root['menu'] = menubar  # 设置菜单栏

    def clockShow(self):
        self.clockPage.pack()
        self.weatherPage.pack_forget()

    def weatherShow(self):
        self.clockPage.pack_forget()
        self.weatherPage.pack()
