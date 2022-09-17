n=int(input("Please tell how many elements you wanna insert into the  list:"))
a=[]
for i in range(n):
    a.append(int(input(f"Please enter element at location {i+1}:")))
for j in range(len(a)):
    if a[j]%5==0 or a[j]%7==0:
        print(a[j])