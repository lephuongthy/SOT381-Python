#nhập một danh sách N số nguyên và in ra số lượng phần tử, danh sách là số nguyên tố
def so_nguyen_to(so):
   if so<2:
      return False
   if so==2:
      return True
   if so%2==0:
      return False
   for i in range(3,int(so**0.5)+1,2):
      if so%i==0:
         return False
   return True
      
n=int(input("nhập giới hạn n của danh sách: "))
a=[]
b=[]
if n<=0:
    print("giới hạn danh sách không hợp lệ")
else:
   for i in range(1,n+1):
       x=int(input("nhập một số nguyên N vào danh sách: "))
       a.append(x)

for z in a:
   if so_nguyen_to(z):
      b.append(z)

print(f"số lượng và các phần tử là số nguyên tố là: {len(b)}")
for y in b:
  print(y)