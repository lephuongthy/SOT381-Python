# kiểm tra xem số n có phải là số hoàn hảo hay không
def tim_uoc(so):
    a=[]
    for i in range(1, so):
        if so%i==0:
           a.append(i)
           b=sum(a)
        return b
    
def tong_so(n):
    if n==tim_uoc(n):
        print(f"số {n} là số hoàn hảo")
    else:
        print(f"số {n} không phải số hoàn hảo")

z=int(input("nhập một số bất kì: "))
if z<=0:
    print(f"số không hợp lệ")
else:
    tong_so(z)
