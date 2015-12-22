#Author DownToSky
#Euler Problem 3
import math
def isPrime(n):
    if (n%2==0 and n!=2) or n<1:
        return False
    else:
        counter =0
        i=1
        while i*i<=n:
            if n%i==0:
                counter = counter+1
            i=i+2
        if counter>1:
            return False
        else:
            return True
            
largestPrime=1
number = 600851475143
for x in range(2,int(math.sqrt( number))):
    if isPrime(x) and number%x==0:
        largestPrime=x
    
print ("final largest prime is: "+str(largestPrime))
