#Author DownToSky
#Euler Problem 16
def removeEmptyStrings(list):
    numOfEmptyStrings = list.count("")
    for i in range(0,numOfEmptyStrings):
        list.remove("")
    return list
    
def MultiplyByTwo(n):
    nums=[str(n)]*2
    sum =""
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
    return  sum

    
multi="1"
for i in range(0,1000):
    multi=MultiplyByTwo(multi)
ans=0
for i in range(0,len(multi)):
    ans+=int(multi[i])
print(str(ans))