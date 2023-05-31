arr=[2,-3,1,7,-2,4,-5,6,2,-3]

n=1
x=0
sum=0

while n!=len(arr)/2:
    res=arr[x]*arr[x+3]-arr[x+2]*arr[x-1]
    sum+=res
    x+=2
    n+=1

print(0.5*sum)
