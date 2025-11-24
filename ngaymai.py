a=int(input("nhap ngay: "))
b=int(input("nhap thang: "))
c=int(input("nhap nam: "))

def cuoi_ngay(ngay):
    if  ngay<31:
        ngay+=1
        print(f"ngay mai la ngay {ngay}/{b}/{c}")
        return ngay
    
def cuoi_thang(ngay, thang):
    if (ngay==30 or ngay==31) and thang<12:
        ngay=1
        thang+=1
        print(f"ngay mai la ngay {ngay}/{thang}/{c}")
        return ngay, thang
    
def cuoi_nam(ngay,thang,nam):
    if ngay== 31 and thang==12:
        ngay=1
        thang=1
        nam+=1
        print(f"ngay mai la ngay {ngay}/{thang}/{nam}")
        return ngay, thang, nam
    
def thang_hai(ngay,thang):
        ngay=1
        thang=3
        print(f"ngay mai la ngay {ngay}/{thang}/{c}")
        return ngay, thang

if 1<=a<=31:
    if b in [1,3,5,7,8,10,12]:
        if a<=31:
         cuoi_ngay(a)
         cuoi_thang(a,b)
         cuoi_nam(a,b,c)

    elif b in [4,6,9,11]:
        if a<=30 and a!=31:
         cuoi_ngay(a)
        if a==30:
         cuoi_thang(a,b) 
    else:
        if b==2:
            if (c%4==0 and c%100!=0) or c%400==0:
                if 1<=a<29:
                    cuoi_ngay(a)
                elif a==29:
                    thang_hai(a,b)
            else:
                if 1<=a<28:
                    cuoi_ngay(a)
                elif a==28:
                    thang_hai(a,b)
else:
    print(f"khong hop le")

    

