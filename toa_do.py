from math import sqrt, pow
a=[]
b=[]
for i in range(1,3):
    x=float(input("nhap toa do cua A: "))
    a.append(x)

for i in range(1,3):
    y=float(input("nhap toa do cua B: "))
    b.append(y)

print(f" toa do cua A la: {a}")
print(f"toa do cua B la: {b}")

print(f"khoang cach giua hai toa do la: {sqrt((pow(b[0]-a[0],2))+pow(b[1]-a[1],2))}")