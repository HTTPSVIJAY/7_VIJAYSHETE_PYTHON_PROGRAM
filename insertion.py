a=[]

print("Enter Number of Elements you want to enter")
n=int(input())
for i in range(0,n):
    a.append(int(input()))
print("Before Sorting : ",a)
for i in range(1, len(a)):  
    j=i-1
    temp=a[i]
    while j>=0 and temp<a[j]:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=temp

print("After Sorting : ",a)