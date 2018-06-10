"""
设计一个算法，计算出N阶乘中尾部零的个数
例如：
    11！ = 39916800  因此应该返回2
"""

# 第一种方法，
# 想到这个问题，有人可能第一反应就是现求出N!,然后再根据求出的结果，
# 最后得出N!的末尾有多少个0。
# class Solution:
#     """
#     @param: n: An integer
#     @return: An integer, denote the number of trailing zeros in n!
#     """
#
#     def jiecheng(self, num):
#         if num == 1:
#             return 1
#         temp = self.jiecheng(num - 1)
#         return temp * num
#
#     def trailingZeros(self, n):
#         # write your code here, try to do it without arithmetic operators.
#         result = self.jiecheng(n)
#         result_str = str(result)
#         count = 0
#         for i in result_str[::-1]:
#             if i == "0":
#                 count += 1
#             else:
#                 break
#         return count
#
# s = Solution()
# print(s.trailingZeros(25))

'--------------------------------------------------------------------------------------------------------'

# 第二种方法：就是看10的组成2和5，然后含有5的数远远小于含有2的数的数量，于是我们只要统计出含有5的数的数量，
# 同时，对于不同的数，对于5的贡献不一样，5,15,20均只贡献1个5，而25会贡献2个5，所以要计算两次，递归找下去
# 下面的代码同样会超时，需要继续优化

class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """

    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        count = 0
        for i in range(5, n + 1):     #  从5开始遍历到这个数
            if i % 5 == 0:    # 是5的倍数就放进来
                while True:
                    if i % 5 == 0:   # 判断这个数可以被多少个5整除
                        count += 1
                        i = i / 5
                    else:
                        break
        return count

s = Solution()
print(s.trailingZeros(1001171717))