#tính tổng các chữ số của số nguyên dương n
n=int(input("nhập một số bất kì: "))
total=0
for i in str(n):
    total+=int(i)
print(f"tổng của các chữ số của {n} là {total}")

