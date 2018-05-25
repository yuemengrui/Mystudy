"""
给定一个数组,编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序
例如：
    输入：[0,1,0,3,12]
    输出：[1,3,12,0,0]
"""


def move_zero(list1):   # 遍历列表，遇到0就删除这个元素，并把它添加到列表末尾
    len1 = len(list1)  # 获取原始列表长度
    for i in range(len1):    # 删除为0的元素
        try:
            list1.remove(0)
        except:
            pass

    for j in range(len1 - len(list1)):   # 在列表末尾添加0，删除了多少个0，就添加多少个0
        list1.append(0)
    return list1


list1 = [0, 2, 0, 0, 1, 0, 2, 0, 0, 0, 6, 0, 9, 0, 3, 12, 0]
print(move_zero(list1))