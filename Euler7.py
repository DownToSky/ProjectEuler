#Author DownToSky
#Euler Problem 7

numberOfPrimes=0
i=2
while i>0:
    j=1
    numberOfDivisbles=0
    while j*j<=i:
        if i%j==0:
           numberOfDivisbles = numberOfDivisbles+1
        j=j+1
    if numberOfDivisbles==1:
        numberOfPrimes=numberOfPrimes+1
    if numberOfPrimes==10001:
        print(str(i))
        break
    if i>2:
        i=i+2
    else:
        i=i+1