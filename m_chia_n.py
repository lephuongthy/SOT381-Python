a=int(input("nhap so nguyen m: "))
b=int(input("nhap so nguyen n: "))
if a>0 and b>0:
    print(f"phan nguyen cua m chia cho n= {a/b}")
    print(f"phan du cua m chia cho n= {a%b}")
else:
    print(f"khong hop le")