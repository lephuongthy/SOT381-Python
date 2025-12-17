#Kiểm tra một số có phải là số Armstrong (tổng lập phương các chữ số bằng chính nó) hay không.
from math import pow
n=int(input("nhập một số bất kì: "))
total=0
for i in str(n):
    total+=pow(int(i),3)
if total==n:
    print(f"số {n} là số Armstrong")
else:
    print(f"số {n} không phải là số Armstrong")