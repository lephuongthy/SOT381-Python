n=int(input("nhập một số bất kì: "))
a=[]
for i in str(n):
    a.append(i)
if a==a[::-1]:
    print(f"{n} là số đối xứng")
else:
    print(f"{n} không phải là số đối xứng")