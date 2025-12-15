#tìm tất cả các ước số của số nguyên dương n
n=int(input("nhập một số bất kì: "))
a=[]
if n<=0:
    print("hãy nhập số nguyên lớn hơn 0")
else:
    for i in range(1,n+1):
        if n%i==0:
            a.append(i)

print(f"các ước số của số {n} là {a}")
