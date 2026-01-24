"""Kiểm tra bộ ba số vừa nhập vào là bộ ba cạnh của loại tam giác nào
(thường, vuông, cân, vuông cân, đều, hay không phải tam giác)"""

a=float(input("nhập cạnh thứ nhất: "))
b=float(input("nhập cạnh thứ hai: "))
c=float(input("nhập cạnh thứ ba: "))
if a>0 and b>0 and c>0 and (a+b)>c and (a+c)>b and (b+c)>a:
    if a==b==c:
        print(f"day la tam giac deu")
    elif a==b!=c or a==c!=b or b==c!=a:
        print(f"day la tam giac can")
    elif pow(a,2)+pow(b,2)==pow(c,2) or pow(b,2)+pow(c,2)==pow(a,2) or\
          pow(a,2)+pow(c,2)==pow(b,2):
        print(f"day la tam giac vuong")
    elif (pow(a,2)+pow(b,2)==pow(c,2) or pow(b,2)+pow(c,2)==pow(a,2) or\
          pow(a,2)+pow(c,2)==pow(b,2)) and (a==b!=c or a==c!=b or b==c!=a):
        print("day la tam giac vuong can")
else:
    print("day khong phai la tam giac")