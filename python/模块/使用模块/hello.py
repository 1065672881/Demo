#! /usr/bin/env python3
# -*- coding: utf-8 -*-


' a Test Module'

__author__ = 'SL'

import sys


def test():
    args = sys.argv
    if len(sys.argv) == 1:
        print("Hello Python")
    elif len(sys.argv) == 2:
        print("Hello: %s" % args[1])
    else:
        print("Too Many Arguments")


if __name__ == '__main__':
    test()

# 使用 _ 不公开函数或者变量
