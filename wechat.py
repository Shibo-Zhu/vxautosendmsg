"""
实现定时自动发送消息
"""

import time
import os
import random
import tkinter as tk
from pywinauto.keyboard import send_keys  # 键盘


class autosendmessage:
    def __init__(self, app_dir):
        self.app_dir = app_dir

    def open_app(self):
        os.startfile(self.app_dir)

    def find(self,contact):
        # 打开微信
        self.open_app()
        time.sleep(1)
        # 进入微信，模拟按键Ctrl+F
        send_keys('^f')
        send_keys(contact)
        time.sleep(0.5)
        send_keys('{ENTER}')  # 回车键必须全部大小
        time.sleep(0.3)

    def sendmessage(self, idx,num):
        # 需要发送的消息内容
        cateen = ['一餐', '二餐', '三餐', '四餐', '五餐', '六餐', '七餐', '玉兰苑']
        emoji = ['/::B', '/::|', '/::<', '/::$', '/::Z', '/::@', '/::Q', '/:,@P', '/::>', '/:dig', '/::*']
        surprise = ['xoxo', 'miss{SPACE}u']
        for i in range(num):
            l = random.randint(0, 7)
            m = random.randint(0, 10)
            k = random.randint(0, 1)
            # 输入聊天内容
            # send_keys(cateen[i])

            if idx == 0:
                send_keys(emoji[m])
            else:
                send_keys(surprise[k])
            # 回车发送消息
            send_keys('{ENTER}')
            time.sleep(0.2)

        # time.sleep(1)
        # exit()  # 退出程序

    def periodicalsendmessage(self, tim):
        while True:
            time_now = time.strftime("%H:%M:%S", time.localtime())  # 获取当前时间
            # sent_time = '22:22:30'  # 发送时间
            sent_time = time_now
            if time_now == sent_time:  # 当前时间等于发送时间则执行以下程序
                self.sendmessage()


if __name__ == "__main__":
    app_dir = r'C:\Program Files (x86)\Tencent\WeChat\WeChat.exe'  # 此处为微信的绝对路径
    sendmsg = autosendmessage(app_dir)
    root = tk.Tk()
    root.title('vx随机发送emoji')

    # 设置标签信息
    label1 = tk.Label(root, text='vx联系人：')
    label1.grid(row=0, column=0)
    label2 = tk.Label(root, text='消息次数：')
    label2.grid(row=1, column=0)

    # 创建输入框
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1, padx=10, pady=5)
    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=1, padx=10, pady=5)


    # 创建按键
    def show():
        print('vx联系人：%s' % entry1.get())
        print('消息次数：%s' % entry2.get())


    def delete():
        entry1.delete(0, 'end')
        entry2.delete(0, 'end')


    def sendemoji():
        contact = entry1.get()
        sendmsg.find(contact)
        sendmsg.sendmessage(0, int(entry2.get()))


    def sendsurprise():
        contact = entry1.get()
        sendmsg.find(contact)
        sendmsg.sendmessage(1, int(entry2.get()))


    button1 = tk.Button(root, text='发送emoji', command=sendemoji).grid(row=3, column=0,
                                                                        sticky=tk.W, padx=30,
                                                                        pady=5)
    button2 = tk.Button(root, text='随机彩蛋', command=sendsurprise).grid(row=3, column=1,
                                                                          padx=30,
                                                                          pady=5)
    button3 = tk.Button(root, text='清空', command=delete).grid(row=3, column=2,
                                                                padx=30, pady=5)
    button4 = tk.Button(root, text='退出', command=root.quit).grid(row=3, column=3,
                                                                   sticky=tk.E, padx=30, pady=5)

    tk.mainloop()
