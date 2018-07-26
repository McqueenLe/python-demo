#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# import itertools as its
# words = "1234568790"
# r =its.product(words,repeat=10)
# dic = open("dic.txt","a")
# for i in r:
#  dic.write("".join(i))
#  dic.write("".join("\n"))
# dic.close()

fo = open("foo.txt", "r")

def createWords(currentWidth,wordslist,lastresultList,totalArray):

    if 1==currentWidth:

        lastresultList=[]

        lastresultList.extend(wordslist)

        totalArray.extend(wordslist);

        return lastresultList;

    else:

        preWords= createWords( currentWidth-1, wordslist, lastresultList,totalPwd)

        lastresultList=[]

        for word in wordslist:

            for lastWord in preWords:

                newResult=word+lastWord

                totalArray.append(newResult)

                lastresultList.append(newResult)

    return lastresultList

# =============================================================================

array = [];

totalPwd= [];

print "========按行读区文件中的数据，每行作为密码的组成单元=============="

for line in fo.xreadlines():

    line = line.strip("\n")

    array.append(line)

print "======================"

print '单元数据共:',len(array),"个"


print "=======以文件中的每一行作为单元来组合密码==============="

xwidth=2 #生成密码的用的元数据个数，生成2个单元的密码，这里可以为大于1的任何整数，

resultWorlds=createWords(xwidth,array,array,totalPwd)

#

print "组成的",xwidth,"位密码共",len(resultWorlds)

print "所有密码共",len(totalPwd),"个(包含1-",xwidth,")位"