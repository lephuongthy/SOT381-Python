#tính tổng của một dãy số có công sai d(cấp số cộng)
day_so=[]
a=int(input("nhap tong so ban muon tinh: "))
for i in range(a):
    so=int(input(f"nhap so thu {i+1}: "))
    day_so.append(so)
print(f"day la day so ban vua nhap: {sorted(day_so)}")
c=sorted(day_so)
b=len(day_so)
d=(c[b-1]-c[0])/(len(c)-1) #công sai
if d==(c[1]-c[0])==(c[2]-c[1]):
    print(f"tong day so vua nhap co cong sai d={d} la: {len(c)/2*(2*c[0]+(len(c)-1)*d)}")
else:
    print(f"day so vua roi khong phai cap so cong")
