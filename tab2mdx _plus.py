#!/usr/bin/python
# -*- coding: <utf-8> -*-

import re

print('made by snowdax at pdawiki')

fileNameInput = input('请输入文件名（不含后缀）：\n> ')
fileName = fileNameInput + '.txt'

fo = open(fileName,'r')
data = fo.read()
fo.close()




RegexEX = re.compile(r'''(
	([^\t\n]{1,})
	(\t)
	([^\t\n]{1,})
	)''', re.VERBOSE)


matches = []
for groups in RegexEX.findall(data):
	
	oldEntry = groups[1] + '\t' + groups[3]
	matches.append(oldEntry)

	newEntry = groups[3] + '\t' + groups[1]
	matches.append(newEntry)

data = '\n'.join(matches)




Regex1 = re.compile('\n')
Regex2 = re.compile('\t')

data = Regex1.sub('\n</>\n', data)
data = Regex2.sub('\n', data)

fileName_forMdxBuilder_plus = fileNameInput + '_forMdxBuilder_plus.txt'
fo = open(fileName_forMdxBuilder_plus, 'w')
fo.write(data)
fo.close()

print('完成！')