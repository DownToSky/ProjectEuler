#By DownToSky
#Euler Problem 29

a_min=b_min=2
a_max=b_max=100


#Making an arrey of tuples
#The first element in the tuple is the base
#and the second is a list of its valid exponents
a=[]
for a_i in range(0,a_max-a_min+1):  # +1 for inclusiveness
    a.append((a_min+a_i,[]))
    for b_i in range(0,b_max-b_min+1):
        a[a_i][1].append(b_min+b_i)

print(a)

    
