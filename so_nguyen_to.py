#đếm các số nguyên tố nhỏ hơn n
def so_nguyen_to(so):
   if so<=1:
      return False
   for i in range(2,so):
      if so%i==0:
         return False
   return True
      
def dem_so(n):
   total=0
   for x in range(2,n):
      if so_nguyen_to(x):
         total+=1
   return total

z=int(input("nhập số giới hạn n của bạn: "))
if z<2:
   print(f"không có số nguyên tố nào nhỏ hơn {z}")
else:
   tong_so=dem_so(z)
   print(f"tổng số nguyên tố nhỏ hơn {z} là {tong_so}")


     