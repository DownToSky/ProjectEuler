#Author DownToSky
#Euler Problem 25

def removeEmptyStrings(list):
    numOfEmptyStrings = list.count("")
    for i in range(0,numOfEmptyStrings):
        list.remove("")
    return list
#returns the sum of two strings in string 
#Look at problem 13
def StringSum(str1,str2):
    sum =""
    nums=[str1,str2]
    while True:
        sumOfLastDigs = 0
        remainder=""
        
        for i in range(0,len(nums)):
            sumOfLastDigs+=int(nums[i][len(nums[i])-1])
            nums[i]=nums[i][0:len(nums[i])-1]
        remainder=str(sumOfLastDigs)[0:len(str(sumOfLastDigs))-1]
    
        nums = removeEmptyStrings(nums)
        if len(nums)==0:
            sum= str(sumOfLastDigs)+sum
            break
        else:
            sumOfLastDigs=sumOfLastDigs%10
            sum = str(sumOfLastDigs)+sum
            if remainder!="":
                nums.append(remainder)
    return sum

#Problem 2 with a little twist
Fn_2= "1"
Fn_1="1"
index=2
while True:
    index+=1
    
    currentFib=StringSum(Fn_1,Fn_2)
    if len(currentFib)==1000:
        print(str(index))
        break
    Fn_2=Fn_1    
    Fn_1=currentFib