# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-06-30 17:09:21
# @Last Modified time: 2016-06-30 17:25:10
# @FileName: a.py


def appendsums(lst):
    for i in range(25):
        lst.append(lst[-1] + lst[-2] + lst[-3])

sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[20]


str = "sss1"
print str.last()