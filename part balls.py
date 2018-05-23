"""
题目：有10个球分别3红、3蓝、4白，现需要将这10个球随机放入这3个盒子，要求每个盒子至少有一个白球，请用程序实现

解题思路：把球分两堆，白球一堆，其他颜色球一堆，分开分配
"""
import random
boxs = [[], [], []]
balls1 = ["red1", "red2", "red3", "blue1", "blue2", "blue3", "blue4"]
balls2 = ["w1", "w2", "w3", "w4"]
while True:
    boxs = [[], [], []]  # 这句很重要，不然的话循环一次之后如果条件不满足要求，会接着循环，里面的元素会重复添加

    for ball2 in balls2:    # 分配白球
        boxs[random.randint(0, 2)].append(ball2)

    if (len(boxs[0]) != 0) and (len(boxs[1]) != 0) and (len(boxs[2]) != 0):  # 判断每个盒子里至少有一个白球
        print("分球OK")
        break

for ball in balls1:   # 分配其他颜色的球
    boxs[random.randint(0, 2)].append(ball)

for i in boxs:   # 打印结果
    print("第%d个盒子里有：" % (boxs.index(i) + 1), end="")

    for j in i:
        print(j, end="  ")
    print()

