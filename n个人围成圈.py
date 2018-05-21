"""
有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出
圈子，问最后留下的是原来第几号的那位。
"""


def fn(n):
    list1 = [i for i in range(1, n + 1)]    # 将人数进行编号排序
    while True:
        if len(list1) <= 2:     # 留下来的人员编号
            return list1
        else:
            del list1[2]        # 删除报数为3的人员
            list1.append(list1[0])     # 重新排列人员编号列表 把前面两个放到列表最后
            list1.append(list1[1])
            del list1[0]
            del list1[0]


n = int(input("请输入人数："))
print(fn(n))

