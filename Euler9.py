#Author DownToSky
#Euler Problem 9
a =0
notDone = True
i=1
while i<1000 and notDone:
    for j in range(i,1000):
        k=1000-i-j
        if i+j<k and i*i+j*j==k*k:
            print ("answer: "+str(i)+" "+str(j)+" "+ str(k))
            notDone=False
            break