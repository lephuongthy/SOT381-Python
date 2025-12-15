#tính tổng chuỗi S=1/a +1/(a+1)... cho đến khi 1/(a+1)<0,0001
a=int(input("nhập một số bất kì: "))
S=0
if a==0:
    print(f"phép chia không hợp lệ")
elif a<0:
    print("hãy nhập số lớn hơn 0 để phép chia có nghĩa")
else:
    while (1/a)>=0.0001:
       S+=1/a
       a+=1
    print(f"tổng chuỗi={S}")