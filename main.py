from mainPage import *
import tkinter as tk


# 主函数
def main():
    root = tk.Tk()
    page = MainPage(root)

    # 开启时钟刷新
    page.clockPage.update()

    #开启界面
    root.mainloop()


if __name__ == '__main__':
    main()


