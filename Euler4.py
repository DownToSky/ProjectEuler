#Author DownToSky
#Euler Problem 4
def isPalindromic(n):
    stringN = str(n)
    leftBound = 0
    rightBound = len(stringN)-1
    isPali = True
    while leftBound<rightBound:
        if stringN[leftBound]!=stringN[rightBound]:
            isPali=False
            break
        rightBound=rightBound-1
        leftBound=leftBound+1
    return isPali

i=999
j=999
isFound = False
largestPoli=0
while i>99:
    j=999
    while j>99:
        if isPalindromic(i*j) and i*j > largestPoli:
            largestPoli=i*j
        j=j-1
    i=i-1

print("answer: "+str(largestPoli))
