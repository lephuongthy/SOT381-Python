#Xuất ra màn hình ước chung lớn nhất và bội chung nhỏ nhất của 2 số m và n

m=int(input("nhập số thứ nhất: "))
n=int(input("nhập số thứ hai: "))

def uoc(so):
    a=set()
    for x in range(1,so+1):
        if so%x==0:
            a.add(x)
    return a

set1=uoc(m)
set2=uoc(n)
uoc_chung=set1&set2
print(f"ước chung lớn nhất của {m} và {n} là: {max(uoc_chung)}")
print(f"bội chung nhỏ nhất của {m} và {n} là: {(m*n)/max(uoc_chung)}")