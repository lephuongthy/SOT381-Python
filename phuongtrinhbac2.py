from math import sqrt
#pt bac 2 ax^2 +bx+c=0
def ptbac1(b,c):
    if b==0:
        if c==0:
            print(f"phuong trinh co vo so ngiem")
        else:
            print(f"phuong trinh vo nghiem")
    else:
        print(f"phuong trinh co nghiem x={-c/b}")

def hainghiem(d,a,b):
    x1=(-b+sqrt(d)/(2*a))
    x2=(-b-sqrt(d)/(2*a))
    print(f"phuong trinh co nghiem x1={x1}")
    print(f"phuong trinh co nghiem x2={x2}")
    return x1, x2

a=float(input("nhap he so a:"))
b=float(input("nhap he so b:"))
c=float(input("nhap he so c:"))
d=b*b-4*a*c
if a==0:
    ptbac1(b,c)
else:
    if d<0:
        print(f"phuong trinh vo nghiem")
    elif d==0:
        print(f"phuong trinh co nghiem kep x1=x2={-b/(2*a)}")
    else:
        hainghiem(d,a,b)
        
