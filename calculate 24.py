import random


def extract_poker():  # 抽取4张扑克牌, extract(抽取)
    poker_list = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]  # 总扑克牌列表
    extract_poker_list = []  # 存放抽取的扑克牌
    for i in range(4):
        index = random.randint(0, 12)
        extract_poker_list.append(poker_list[index])
    print("抽取的4张牌为：", extract_poker_list)

    index = -1
    for i in extract_poker_list:  # 把扑克牌全部换成数字
        index += 1
        if i == "J" or i == "Q" or i == "K":
            extract_poker_list[index] = "10"
        if i == "A":
            extract_poker_list[index] = "1"
        extract_poker_list[index] = eval(extract_poker_list[index])
    # print(extract_poker_list)
    return extract_poker_list


def operation(x, y):
    operation_list = {"+": x+y, "-": x-y, "--": y-x, "*": x*y}  # 运算列表,计算两个数的值
    if x != 0 and y != 0:
        operation_list["/"] = float(x/y)
        operation_list["\\"] = float(y/x)
    return operation_list


def calculate(ep_list):  # 计算24点
    for i0 in range(4):  # 循环获取4张牌，并打乱顺序，可以获取到每张牌，并且没有顺序，相当于随机获取这4个数的顺序
        for i1 in range(4):
            if i1 == i0:
                continue
            else:
                for i2 in range(4):
                    if i2 == i1 or i2 == i0:
                        continue
                    else:
                        for i3 in range(4):
                            if i3 == i2 or i3 == i1 or i3 == i0:
                                continue
                            else:
                                """接下来计算24点，先把两个数传入运算列表，计算出值，再传入第三个数，计算出值，再传入第4个数，计算出最终值"""
                                # 传入两个数，计算结果
                                operation_list1 = operation(ep_list[i0], ep_list[i1])

                                for k1 in operation_list1:  # k1为运算符，可以在下面获取对应得值
                                    """传入第3个数，与前2个数的值进行运算得出结果"""
                                    operation_list2 = operation(operation_list1[k1], ep_list[i2])
                                    for k2 in operation_list2:
                                        """传入第4个数，与前3个数的值进行运算得出结果"""
                                        operation_list3 = operation(operation_list2[k2], ep_list[i3])
                                        for k3 in operation_list3:   # 获取运算符
                                            if operation_list3[k3] == 24:
                                                print("((%d%s%d)%s%d)%s%d = 24" % (ep_list[i0], k1, ep_list[i1], k2, ep_list[i2], k3, ep_list[i3]))
                                                if k1 == "--":
                                                    print("((%d-%d)%s%d)%s%d = 24" % (ep_list[i1], ep_list[i0], k2, ep_list[i2], k3, ep_list[i3]))
                                                if k1 == "\\":
                                                    print("((%d/%d)%s%d)%s%d = 24" % (ep_list[i1], ep_list[i0], k2, ep_list[i2], k3, ep_list[i3]))
                                                if k2 == "--":
                                                    print("(%d-(%d%s%d))%s%d = 24" % (ep_list[i2], ep_list[i0], k1, ep_list[i1], k3, ep_list[i3]))
                                                if k2 == "\\":
                                                    print("(%d/(%d%s%d))%s%d = 24" % (ep_list[i2], ep_list[i0], k1, ep_list[i1], k3, ep_list[i3]))
                                                if k3 == "--":
                                                    print("%d-((%d%s%d)%s%d) = 24" % (ep_list[i3], ep_list[i0], k1, ep_list[i1], k2, ep_list[i2]))
                                                if k3 == "\\":
                                                    print("%d/((%d%s%d)%s%d) = 24" % (ep_list[i3], ep_list[i0], k1, ep_list[i1], k2, ep_list[i2]))
                                                return True
    return False


def main():
    print("这是一个抽取4张扑克牌，计算24点的小游戏")
    print("好好学习，天天向上")
    print("沉迷学习，无法自拔")
    extract_poker_list = extract_poker()
    if not calculate(extract_poker_list):
        print("无解")


if __name__ == '__main__':
    main()

