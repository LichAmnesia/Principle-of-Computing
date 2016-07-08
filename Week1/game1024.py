# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-07-08 09:41:21
# @Last Modified time: 2016-07-08 10:41:40
# @FileName: game1024.py
"""
a game of 1024 for week 1 mini-project
http://www.codeskulptor.org/#user41_5Dup1EVubJ_3.py
Score: 86.0/100
"""

# Merge function for 2048 game.


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = line[:]
    flag = [0] * len(line)
    for round in range((len(result) + 1) / 2):
        move(result, flag)
        check(result, flag)
    return result

# move element to left


def move(line, flag):
    for i in range(len(line)):
        if line[i] != 0:
            continue
        for j in range(i + 1, len(line)):
            if line[j] != 0:
                line[i] = line[j]
                flag[i] = flag[j]
                line[j] = 0
                break
    return line

# merge result


def check(line, flag):
    for i in range(len(line) - 1):
        if line[i] == line[i + 1] and flag[i] + flag[i + 1] == 0:
            line[i] = line[i] * 2
            line[i + 1] = 0
            flag[i] = 1
            flag[i + 1] = 1
            return

# test 1


# def test1():
#     line = [0, 0, 2, 0]
#     expect_line = [2, 0, 0, 0]
#     result_line = merge(line)
#     print "test 1: ", result_line
#     print cmp(result_line, expect_line)


# def test2():
#     line = [2, 0, 2, 4]
#     expect_line = [4, 4, 0, 0]
#     result_line = merge(line)
#     print "test 2: ", result_line
#     print cmp(result_line, expect_line)


# def test3():
#     line = [0, 0, 2, 2]
#     expect_line = [4, 0, 0, 0]
#     result_line = merge(line)
#     print "test 3: ", result_line
#     print cmp(result_line, expect_line)


# def test4():
#     line = [2, 2, 2, 2, 2]
#     expect_line = [4, 4, 2, 0, 0]
#     result_line = merge(line)
#     print "test 4: ", result_line
#     print cmp(result_line, expect_line)


# def test5():
#     line = [8, 16, 16, 8]
#     expect_line = [8, 32, 8, 0]
#     result_line = merge(line)
#     print "test 5: ", result_line
#     print cmp(result_line, expect_line)



# if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
