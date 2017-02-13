# coding: utf-8

# 倒序输出字符串
'''
def output(str1, long1):
    if long1 == 0:
        return
    else:
        print str1[long1 - 1],
        output(str1, long1 - 1)
str1 = raw_input("enter a string: ")
long1 = len(str1)
output(str1, long1)
'''

# 计算程序耗时
'''
import time
start_time = time.clock()
current_time = time.strftime("当前时间：%H:%M %y-%m-%d", time.localtime())
print current_time
time.sleep(4)
end_time = time.clock()
print "程序耗时%.2fs" % (end_time - start_time)
'''

# 打印*号三角形 # 乘法口诀
'''
for i in range(10):
    for j in range(8-i+1):
        print " ",
    for k in range(2*i-1):
        print "*",
    print


for i in range(1, 10):
    for j in range(1, i+1):
        print "%d*%d=%d" % (j, i, j*i),
    print
'''

# excel操作练习
'''
import xlrd
data = xlrd.open_workbook("d:\\test.xlsx")
table = data.sheet_by_index(0)
row_2 = table.row_values(1)
print row_2
for i in row_2:
    print i

'''

# 判断5位的回文数
'''
a = int(raw_input("请输入一个数字:\n"))
x = str(a)
flag = True

for i in range(len(x) / 2):
    if x[i] != x[-i - 1]:
        flag = False
        break
if flag:
    print "%d 是一个回文数!" % a
else:
    print "%d 不是一个回文数!" % a
'''

# 倒序输出列表的值
'''
a = ['one', 'two', 'three']
for i in a[::-1]:
    print i

# a = [0,1,2,3,4,5,6,7,8,9] b = a[i:j] 表示复制a[i]到a[j-1]，
# 以生成新的list对象 b = a[1:3] 那么，b的内容是 [1,2] 当i缺省时，
# 默认为0，即 a[:3]相当于 a[0:3] 当j缺省时，默认为len(alist),
# 即a[1:]相当于a[1:10] 当i,j都缺省时，a[:]就相当于完整复制一份a了
#
# b = a[i:j:s]这种格式呢，i,j与上面的一样，但s表示步进，缺省为1.
# 所以a[i:j:1]相当于a[i:j] 当s<0时，i缺省时，默认为-1. j缺省时，
# 默认为-len(a)-1 所以a[::-1]相当于 a[-1:-len(a)-1:-1]，
# 也就是从最后一个元素到第一个元素复制一遍。所以你看到一个倒序的东东。
'''

# 求素数
'''
for i in range(2, 101):
    flag = 1
    for j in range(2, i / 2 + 1):
        if i % j == 0 and i != j:
            flag = 0
    if flag == 1:
        print i,
'''

# 冒泡排序

def bubble(bubblelist):
    listlength = len(bubblelist)
    while listlength > 0:
        for i in range(listlength - 1):
            if bubblelist[i] > bubblelist[i + 1]:
                # bubblelist[i] = bubblelist[i] + bubblelist[i + 1]
                # bubblelist[i + 1] = bubblelist[i] - bubblelist[i + 1]
                # bubblelist[i] = bubblelist[i] - bubblelist[i + 1]
                temp = bubblelist[i]
                bubblelist[i] = bubblelist[i + 1]
                bubblelist[i + 1] = temp
        listlength -= 1
    print bubblelist


if __name__ == '__main__':
    bubblelist = [3, 4, 1, 2, 12, 7, 18, 12, 5, 8, 0]
    bubble(bubblelist)


# 使用lambda来创建匿名函数
'''
maximum = lambda x,y :  (x > y) * x + (x < y) * y
minimum = lambda x,y :  (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print 'the largar one is %d' % maximum(a,b)
    print 'the lower one is %d' % minimum(a,b)
'''

# random模块使用
'''
import random
print random.random()     # 输出0到1之间的一个随机浮点数0 =< n < 1
print random.uniform(1, 10)     # 输出1到10之间的一个随机浮点数 1 =< n < 10
print random.randint(1, 10)     # 输出1到10之间的一个随机整数 1 =< n <= 10
print random.randrange(1, 100, 2)   # random.randrange([start], stop[, step])，
                                    # 从指定范围内，按指定基数递增的集合中 获取一个随机数。
                                    # 如：random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, ... 96, 98]
                                    # 序列中获取一个随机数。random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效。
print random.choice(("Tuple", "List", "Dict"))  # 从序列，元组或字符串中随机取一个值
print random.choice(['dic1', 'dic2', 'dic3', 'dic4'])

p = ["Python", "is", "powerful", "simple", "andsoon..."]
random.shuffle(p)   # 将一个列表中的元素顺序打乱
print p

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice1 = random.sample(list1, 5)   # 从list1中随机获取5个元素，作为一个片断返回
print slice1
print list1   # 原有序列并没有改变
'''

'''
if __name__ == '__main__':
    from Tkinter import *
    x = 360
    y = 160
    top = y - 30
    bottom = y - 30

    canvas = Canvas(width=400, height=600, bg='white')
    for i in range(20):
        canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()
'''
'''
if __name__ == '__main__':
    from Tkinter import *
    canvas = Canvas(width=500, height=600, bg='white')
    left = 20
    right = 50
    top = 50
    num = 15
    for i in range(num):
        canvas.create_oval(250 - right, 250 - left, 250 + right, 250 + left)
        canvas.create_oval(250 - 20, 250 - top, 250 + 20, 250 + top)
        canvas.create_rectangle(20 - 2 * i, 20 - 2 * i, 10 * (i + 2), 10 * (i + 2))
        right += 5
        left += 5
        top += 10

    canvas.pack()
    mainloop()
'''

