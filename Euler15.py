#Author DownToSky
#Euler Problem 15

#Sadly the answer for this problem for xPosFinal=20 and yPosFinal=20  is REALLY BIG
def numsOfRoutes(x,y,xFinal,yFinal):
    if x==xFinal or y==yFinal:
        return 1
    else:
        return numsOfRoutes(x+1,y,xFinal,yFinal)+numsOfRoutes(x,y+1,xFinal,yFinal)
        
xPosFinal=12
yPosFinal=12
xPosStart=0
yPosStart=0
print(str(numsOfRoutes(xPosStart,yPosStart,xPosFinal,yPosFinal)))