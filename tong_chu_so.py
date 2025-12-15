#tính tổng các chữ số của số nguyên dương n
n=int(input("nhập một số bất kì: "))
a=[]
for i in str(n):
    a.append(i)
print(f"tổng chữ số của số {n} là {len(a)}")
