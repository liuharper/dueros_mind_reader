#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/17

"""
    desc:pass
"""
from dueros.directive.Display.tag.BaseTag import BaseTag
from dueros.directive.Display.tag import TagTypeEnum


class AmountTag(BaseTag):

    def __init__(self, amount):
        BaseTag.__init__(self, TagTypeEnum.TAG_TYPE_AMOUNT, amount)


if __name__ == '__main__':
    pass