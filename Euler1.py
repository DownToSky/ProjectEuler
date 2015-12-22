#Author DownToSky
#Euler Problem 1
sum = 0
for x in range(1,1000):
    if x%3==0:
        sum = sum+x
    else:
        if x%5==0:
            sum = sum+x
print (str(sum))