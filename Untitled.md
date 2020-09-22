

```python
import random
s=random.randint(10,50) #随机生成参与游戏的总人数
print("一共有" + str(s) + "个人参加")
m=(input("请选择你的站位："))
t=3 #报到3的人淘汰
list1=[i for i in range(1,s+1)]
 #自定义一个函数，步长为2 用while运用 报数123，将前面两个一次放到列表的最末尾，然后删除列表的第一位（也就是报到数字3的人）
    #如此反复一直到列表只剩下两个
def move(list1, sep):
    for i in range (sep):
        a = list1.pop(0)
        list1.append(a) 
while len(list1) > 2:
    move(list1, 2)
    list1.pop(0)
c,d =list1
print("最后剩下的两个站位：" + str(c) + "，" + str(d))
if m == c or m == d:
    print("You win")
else:
    print("You lost")
```


```python

```
