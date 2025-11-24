#tìm số lớn nhất trong ba số

x=[1,2,3]
y=[]
for i in range(1):
    for u in x:
        so=float(input(f"nhập số thứ {u}: "))
        y.append(so)
print(f"số lớn nhất trong ba số là: {max(y)}")
