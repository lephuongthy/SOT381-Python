z=int(input("nhập một số bất kì: "))
a=[]
if z<=0:
    print(f"số không hợp lệ")
else:
    for i in range(1,z):
        if z%i==0:
            a.append(i)
        
if z==sum(a):
    print(f"số {z} là số hoàn hảo")
else:
    print(f"số {z} là số không hoàn hảo")