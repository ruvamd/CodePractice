def evenIntFunc(n):
    result=[]
    for i in range(n):
        if i%2==0:
            result.append(i)
    return result
n=int(input('Enter the number: '))
print(evenIntFunc(n))