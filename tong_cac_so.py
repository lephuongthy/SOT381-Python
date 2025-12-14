#tính tổng các số từ 1 đến n (với n là giá trị tự chọn)
n=int(input("nhập giá trị cuối cùng trong dãy số bạn muốn tính:"))
total=0
x=1
while x<=n:
   total+=x
   x+=1
print(f"tổng các số từ 1 đến {n} là: {total}")

