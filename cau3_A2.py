#nhập một danh sách N số nguyên và in ra tổng của phần tử ở vị trí chẵn
n=int(input("nhập giới hạn n của danh sách: "))
a=[]
if n<=0:
    print("giới hạn danh sách không hợp lệ")
else:
   for i in range(1,n+1):
       x=int(input("nhập một số nguyên N vào danh sách: "))
       a.append(x)

b=a[::2]

print(f"tổng của phần tử ở vị trí chẵn là: {sum(b)}")