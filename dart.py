#!/usr/bin/env python
# -*- coding: utf-8 -*-

totalRound = 20
totalScore = 501
person = 2

scores = [totalScore] * person

for i in range(0, totalRound):
    print("")
    print(u'第 %d 局：' % (i + 1))
    for j in range(0, person):
        curScore = input(u'%d:' % (j + 1))
        if scores[j] - curScore > 0:
            scores[j] -= curScore
        elif scores[j] == curScore:
            scores[j] -= curScore
            break
    if j < (person - 1) or scores[j] == 0:
        break
    for j in range(0, person):
        print(u"玩家 %d ：%d" % ((j+1), scores[j]))


minI = -1
minV = 501
for j in range(0, person):
    if scores[j] < minV:
        minV = scores[j]
        minI = j
print(u"游戏结束，玩家 %d 获胜！" % (minI+1))

