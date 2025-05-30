z=input()
arr=[]
number=[]
for i in range(len(z)):
    j=0
    flag=False
    if (len(arr)==0):
        arr.append(z[i])
    else:
        for j in range(len(arr)):
            if arr[j]==z[i]:
                flag=True
                break
        if flag==True:
            number.append(len(arr))
            arr=arr[j+1:]
            arr.append(z[i])
        else:
            number.append(len(arr))
            arr.append(z[i])
number.append(len(arr))
print(max(number))