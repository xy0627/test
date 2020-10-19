#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tkinter
top = tkinter.Tk()
# 进入消息循环
top.mainloop()


# In[1]:


from tkinter import *
import random
import tkinter.messagebox 
root = Tk()#创建根窗口
root.title('猜数字游戏')#设置窗口标题
root.minsize(300,200)#设置窗口大小master.minsize(height, width)
n=random.randint(1,100)



def check_num():#定义一个check_num函数
    guess=text_guess.get()
    guess=int(guess)
    if guess >  n:
        tkinter.messagebox.showinfo("height","你的答案太大了.")#语法 MessageBox (text,title{,icon{,button{,default}}})
    if guess < n:
        tkinter.messagebox.showinfo("low","你的答案太小了.")
    if guess == n:
        tkinter.messagebox.showinfo("good","猜对了!")
        

label_name=tkinter.Label(root,text="欢迎来到猜数字游戏!")
label_name.place(x=80,y=60)



label_guess=tkinter.Label(root,text='请输入你的答案:')#Label，按钮控件；可以显示文本和位图
label_guess.place(x=10,y=150)#输入label所在位置
text_guess=tkinter.Entry(root,width=10)#Entry，输入控件；用于显示简单的文本内容
text_guess.place(x=110,y=150)#输入text所在位置
btnCheck=tkinter.Button(root,text='Guess',command=check_num)#Button，按钮控件；在程序中显示按钮。
btnCheck.place(x=200,y=150,width=45,height=28)#输入button的位置

 
root.mainloop();


# In[ ]:





# In[ ]:




