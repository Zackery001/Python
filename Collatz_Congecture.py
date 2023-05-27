array=[]
n=1
def d_by2(num):
    if (num % 2) == 0:
        return True
while n==1:
    user_int=float(input("Please enter a int :"))
    array.append(user_int)
    bullshit=int(user_int)
    while n==1:
        if d_by2(user_int)==True:
            user_int=user_int/2
            if user_int in array:
                print(f"{bullshit}={array}")
                break
            else:
                array.append(user_int)
        else: 
            user_int=user_int*3+1
            if user_int in array:
                print(f"{bullshit}={array}")
                break
            else:
                array.append(user_int)