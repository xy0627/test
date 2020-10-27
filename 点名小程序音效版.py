
# coding: utf-8

# In[1]:


from tkinter import *
import random
import threading
import time
import tkinter
import pygame as py

#import os
#path=r"C:\Users\Administrator\Desktop\转场音效_.wav"
#os.system("mpg123"+path)

# 初始化窗口
root = Tk()
root.title("随机名单")
root.geometry('400x400')
root.resizable(False, False)
root.flag = True
label_name = tkinter.Label(root, text="请开始点名!")
label_name.place(x=150, y=50)
label_name['fg'] = 'blue'

# 三个Lable标签
first = tkinter.Label(root, text='', font=("楷体", 15, "normal"))
first.place(x=130, y=140, width=120, height=100)

second = tkinter.Label(root, text='', font=("宋体", 20, "normal"))
second.place(x=130, y=220, width=120, height=100)

third = tkinter.Label(root, text='', font=("楷体", 15, "normal"))
third.place(x=130, y=300, width=120, height=100)

students = ['1:周嘉铖', '2:钱珑超', '3:徐展', '4:尤桉哲', '5:钱涛', '6:黄舒怡', '7:胡志辉', '8:吴昭耀',
            '9:陈萌萌', '10:郑巧悦', '11:陈艳', '12:梁明皓', '13;蒋俊超', '14:徐颖', '15:倪宏涛', '16:潘梦倩',
            '17:俞靖庐', '18:王中阳', '19:毛贞强', '20:张嫒', '21:朱速航', '22:陈涛', '23:陆元超', '24:叶振雄',
            '25:奚申杰', '26:叶梦婷', '27:徐丽丽', '28:潘艳']

def switch():
    root.flag = True
    while root.flag:
        i = random.randint(0, len(students) - 1)
        first['text'] = second['text']
        second['text'] = third['text']
        third['text'] = students[i]
        time.sleep(0.1)  # 表示进程挂起的时间


# 开始按钮
def butStartClick():
    t = threading.Thread(target=switch)
    t.start()
    import pygame as py
    py.mixer.init()
    py.mixer.music.load(r'C:\Users\Administrator\Desktop\实用音效-未整理-039.欢畅背景音乐-A2_01019.m_爱给网_aigei_com.mp3')
    py.mixer.music.play(-1, 50)# 播放  第一个是播放值 -1代表循环播放， 第二个参数代表开始播放的时间


btnStart = tkinter.Button(root, text='开始', command=butStartClick )
btnStart.place(x=100, y=120, width=55, height=40)


# 结束按钮
def btnStopClick():
    root.flag = False
    py.quit()


butStop = tkinter.Button(root, text='停止', command=btnStopClick )
butStop.place(x=240, y=120, width=55, height=40)
#def music():
   #import winsound
   #winsound.PlaySound(r'C:\Users\Administrator\Desktop\转场音效_.wav',winsound.SND_FILENAME)
   #winsound.Beep(32767, 152212)
#btnmusic =tkinter.Button(root,text='音乐',command=music)
#btnmusic.place(x=280, y=120, width=55, height=40)

# 启动主程序
# 是当前模块名，当模块被直接运行时模块名为 __main__ 。这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。

mainloop()

