a=int(input("nhap he so a:"))
b=int(input("nhap he so b:"))
c=int(input("nhap he so c:"))
if a>b:
    if b>c:
        print(f"{a} la so lon nhat")
    elif c>a:
        print(f"{c} la so lon nhat")    
else:
    if a>c:
        print(f"{b} la so lon nhat")
    elif c>b:
        print(f"{c} la so lon nhat")