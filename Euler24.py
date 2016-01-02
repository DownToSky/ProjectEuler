#Author DownToSky
#Euler Problem 24
import copy

def orderInLexicographic(orderedList):
    if len(orderedList)==1:
        return [[orderedList[0]]]
    listInLexic=[]
    for i in range(0,len(orderedList)):
        tempList=copy.deepcopy(orderedList)
        tempNum=tempList.pop(i)
        lexicListsOfRemaining=orderInLexicographic(tempList)
        for j in range(0,len(lexicListsOfRemaining)):
            listInLexic.append([tempNum]+lexicListsOfRemaining[j])
    return listInLexic


print(orderInLexicographic([0,1,2,3,4,5,6,7,8,9])[1000000-1])

