def numOfDivisors(n):
    count =0
    for i in range (1,int(n/2+1)):#the highest diviso of n excluding n is n/2
        if n%i==0:
            count +=1
    return count+1#n is also a divisor of n

i=1
triagNum=0
while True:
    triagNum+=i
    if numOfDivisors(triagNum)>500:
        print (str(triagNum))
        break
    i+=1
