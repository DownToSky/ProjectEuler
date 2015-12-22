#Author DownToSky
#Euler Problem 9
def arePythagTriplet(a,b,c):
    if a*a+b*b==c*c:
        return True
    else:
        return False

for a in range(1,int(1001/3)):
    for b in range(a,int(1001/2)):
        c=1000-a-b
        if arePythagTriplet(a,b,c):
            print(str(a*b*c))