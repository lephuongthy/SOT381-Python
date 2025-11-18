x=int(input("nhap so giay: "))
if x>0:
    a=x//3600
    b=a//60
    c=x-(a*3600)
    print(f"{x} giay bang {a} gio,{b} phut,{c} giay")