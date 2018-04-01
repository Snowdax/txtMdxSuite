#!/usr/bin/python
# -*- coding: <utf-8> -*-

import re

print('made by snowdax at pdawiki')

fileNameInput = input('请输入文件名（不含后缀）：\n> ')
fileName = fileNameInput + '.txt'

fo = open(fileName,'r')
data = fo.read()
fo.close()

Regex1 = re.compile('\n')
Regex2 = re.compile('\t')

data = Regex1.sub('\n</>\n', data)
data = Regex2.sub('\n', data)

fileName_forMdxBuilder = fileNameInput + '_forMdxBuilder.txt'
fo = open(fileName_forMdxBuilder, 'w')
fo.write(data)
fo.close()

print('完成！')