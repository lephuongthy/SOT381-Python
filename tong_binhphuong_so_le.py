#tính tổng bình phương các số lẻ từ 1 đến n(với n là giới hạn tự chọn)

x=1
total=0
n=int(input("nhập giới hạn n: "))
if n>0:
    total+=x
while x<=n:
    x+=1
    if x%2!=0:
        total+=x**2
print(total)