from tkinter import *
import math, time
import threading as thd
from getWeather import *


class clockPage(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        # 预定义变量
        self.root = master  # 定义内部变量root
        self.root.geometry("400x500")
        self.canvas = Canvas(self, width=400, height=500)
        self.canvas.pack()
        self.List = []

        # 配置时钟边框
        # 生成外圆，圆内填充颜色是白色
        self.canvas.create_oval(50, 50, 350, 350, fill='white')
        # 画出刻度
        self.points()

        # 显示指针和时间
        self.createPage()

    def update(self):
        for j in self.List:
            self.canvas.delete(j)
        # print('update')
        self.createPage()
        handle = thd.Timer(0.5, self.update)
        handle.daemon = True
        handle.start()

    def createPage(self):
        tm = time.localtime()  # 获取当前时间
        t_hour = 0
        # 转换成12小时制
        if tm.tm_hour <= 12:
            t_hour = tm.tm_hour
        else:
            t_hour = tm.tm_hour - 12
        # 定义指针大小
        rad1 = 2 * math.pi * (t_hour + tm.tm_min / 60) / 12  # 时针
        rad2 = 2 * math.pi * (tm.tm_min + tm.tm_sec / 60) / 60  # 分针
        rad3 = 2 * math.pi * tm.tm_sec / 60  # 秒针
        # 画指针
        self.createline(50, 6, rad1)  # 时针
        self.createline(90, 3, rad2)  # 分针
        self.createline(120, 1, rad3)  # 秒针
        # 显示数字时间
        cur_time = time.strftime('%Y-%m-%d\n\n %X', time.localtime())
        time_text = self.canvas.create_text(200, 420, text=cur_time, font=10, fill='purple')
        self.List.append(time_text)

    # 定义时针上的刻度1~12
    def points(self):
        # 绘制表盘数字
        for i in range(1, 13):
            # 表盘中心的位置是200,200，由此计算刻度的位置
            x = 200 + 120 * math.sin(2 * math.pi * i / 12)
            y = 200 - 120 * math.cos(2 * math.pi * i / 12)
            self.canvas.create_text(x, y, text=i, font=('黑体', 18), fill='Navy')  # 颜色是海军蓝
        # 绘制表盘刻度
        for i in range(1, 61):  # 定义时针刻度（1~12h）
            if i % 5 == 0:  # 5的倍数要长一些
                r = 150
            else:
                r = 145
            x = 200 + 140 * math.sin(2 * math.pi * i / 60)
            y = 200 - 140 * math.cos(2 * math.pi * i / 60)
            x2 = 200 + r * math.sin(2 * math.pi * i / 60)
            y2 = 200 - r * math.cos(2 * math.pi * i / 60)
            self.canvas.create_line(x, y, x2, y2)

    def createline(self, radius, line_width, rad):
        x = 200 + radius * math.sin(rad)
        y = 200 - radius * math.cos(rad)
        i = self.canvas.create_line(200, 200, x, y, width=line_width, fill='black')
        self.List.append(i)


class weatherPage(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.root.geometry("400x500")
        self.createPage()

    def createPage(self):
        Label(self, text='天气页面,还没有设计怎么做UI').pack()
        obj = getWeather()
        if obj['error_code']:
            Label(self, text=obj['reason']).pack()
        else:
            for keys in obj['result']['realtime']:
                Label(self, text="%s : %s" % (keys, obj['result']['realtime'][keys])).pack()
