#Author DownToSky
#Euler Problem 2

#Recursinve approach is not recommended for this problem since
#it has to find the previous fib numbers when the next
#fib number is going to be re-evaluated
#We can define fibbonacci sequence by:
#fib(1)=1
#fib(2)=1
#fib(i)=fib(i-1)+fib(i-2)
#Hence, by storing the last two fibNumbers the next fibonaci number
#can be found
fibPointer1 = 1         #This is always the last fib number found: fib(i-1)
fibPointer2 = 1         #This is always the second last fib number found: fib(i-2)
sum=0                   #Contains the final answer

while fibPointer1<4000000:
    if fibPointer1%2==0:
        sum= sum+fibPointer1
    
    #Finding the next fib number based one the last two:
    nextFib = fibPointer1+fibPointer2   
    
    #Updating the fib(i-1) and fib(i-2):
    fibPointer2=fibPointer1
    fibPointer1=nextFib
    
print (str(sum))