"""
在一个给定的数组中，总是存在一个最大元素。
查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
如果是，则返回最大数字的索引，否则返回-1.
"""
import copy


def greater_number(list1):
    list2 = copy.deepcopy(list1)
    list2.sort()
    if list2[-1] >= list2[-2] * 2:
        return list1.index(list2[-1], 0, len(list1))
    else:
        return -1


list1 = [1, 6, 8, 100, 36, 5, 9, 5]
print(greater_number(list1))