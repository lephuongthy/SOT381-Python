from math import sqrt,pow
def chuvi(a,b,c):
    print(f"chu vi tam giac la: {a+b+c}")

def Stamgiac(a,b,c):
    p=(a+b+c)/2
    print(f"dien tich tam giac la: {sqrt(p*(p*a)*(p*b)*(p*c))}")

def Stamgiacvuong(a,b,c):
    if pow(a,2)+pow(b,2)==pow(c,2):
        print(f"dien tich tam giac la: {1/2*a*b}")
    elif  pow(b,2)+pow(c,2)==pow(a,2):
        print(f"dien tich tam giac la: {1/2*c*b}")
    else:
        print(f"dien tich tam giac la: {1/2*a*c}")

a=float(input("nhap do dai canh thu nhat: "))
b=float(input("nhap do dai canh thu hai: "))
c=float(input("nhap do dai canh thu ba: "))
if a>0 and b>0 and c>0 and (a+b)>c and (a+c)>b and (b+c)>a:
    if a==b==c:
        print(f"day la tam giac deu")
        chuvi(a,b,c)
        Stamgiac(a,b,c)
    elif a==b!=c or a==c!=b or b==c!=a:
        print(f"day la tam giac can")
        chuvi(a,b,c)
        Stamgiac(a,b,c)
    elif pow(a,2)+pow(b,2)==pow(c,2) or pow(b,2)+pow(c,2)==pow(a,2) or\
          pow(a,2)+pow(c,2)==pow(b,2):
        print(f"day la tam giac vuong")
        chuvi(a,b,c)
        Stamgiacvuong(a,b,c)