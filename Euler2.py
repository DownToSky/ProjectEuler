#Author DownToSky
#Euler Problem 2
fibPointer1 = 1
fibPointer2 = 1
sum=0
while fibPointer1<4000000:
    if fibPointer1%2==0:
        sum= sum+fibPointer1
        
    nextFib = fibPointer1+fibPointer2
    fibPointer2=fibPointer1
    fibPointer1=nextFib
print (str(sum))