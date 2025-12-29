#nhập một danh sách N số nguyên và in ra tổng của phần tử có giá trị chẵn
n=int(input("nhập giới hạn n của danh sách: "))
a=[]
b=[]
if n<=0:
    print("giới hạn danh sách không hợp lệ")
else:
   for i in range(1,n+1):
       x=int(input("nhập một số nguyên N vào danh sách: "))
       a.append(x)

for u in a:
    if u%2==0:
        b.append(u)

print(f"tổng của phần tử có giá trị chẵn là: {sum(b)}")