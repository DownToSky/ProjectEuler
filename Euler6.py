#Author DownToSky
#Euler Problem 6
firstSum =0
secondSum =0
for x in range(1, 101):
    firstSum=firstSum+ x*x
    secondSum=secondSum+ x
secondSum=secondSum*secondSum
print (str(secondSum-firstSum))