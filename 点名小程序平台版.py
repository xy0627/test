#!/usr/bin/env python
# coding: utf-8

# In[5]:


from tkinter import *
import random
import threading
import time
import tkinter
#初始化窗口
root=Tk()
root.title("随机名单")
root.geometry('400x400')
root.resizable(False,False)
root.flag = True
label_name=tkinter.Label(root,text="请开始点名!")
label_name.place(x=150,y=50)
label_name['fg'] = 'blue'

#三个Lable标签
first = tkinter.Label(root,text='',font = ("楷体", 15,"normal"))
first.place(x=130,y=140,width=120,height=100)

second = tkinter.Label(root,text='',font = ("楷体", 15,"normal"))
second.place(x=130,y=220,width=120,height=100)

third = tkinter.Label(root,text='',font = ("楷体", 15,"normal"))
third.place(x=130,y=300,width=120,height=100)


students=['1:周嘉铖','2:钱珑超','3:徐展','4:尤桉哲','5:钱涛','6:黄舒怡','7:胡志辉','8:吴昭耀',
          '9:陈萌萌','10:郑巧悦','11:陈艳', '12:梁明皓','13;蒋俊超','14:徐颖','15:倪宏涛','16:潘梦倩',
          '17:俞靖庐','18:王中阳','19:毛贞强','20:张嫒','21:朱速航','22:陈涛','23:陆元超','24:叶振雄',
          '25:奚申杰','26:叶梦婷','27:徐丽丽','28:潘艳']

def switch():
    root.flag=True
    while root.flag:
        i=random.randint(0, len(students)-1)
        first['text']=second['text']
        second['text']=third['text']
        third['text']=students[i]
        time.sleep(0.1)#表示进程挂起的时间


#开始按钮
def butStartClick():
    t=threading.Thread(target=switch)
    t.start()
btnStart=tkinter.Button(root,text='开始',command=butStartClick)
btnStart.place(x=100, y=120, width=55, height=40)

#结束按钮
def btnStopClick():
    root.flag=False
    
butStop=tkinter.Button(root,text='停止',command=btnStopClick)
butStop.place(x=240, y=120, width=55, height=40)

#启动主程序
root.mainloop()


# In[ ]:




