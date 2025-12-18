#Phân tích số nguyên dương thành tích các thừa số nguyên tố
n=int(input("nhập một số bất kì: "))
a=n
b=[]

def so_nguyen_to(x):
    if x<2:
        return False
    for y in range(2,int(x**0.5)+1):
        if x%y==0:
            return False
    return True

for i in range(2,n+1):
    if n%i==0:
        if so_nguyen_to(i):
            while a%i==0:
                b.append(str(i))
                a//=i


print(f"{n}={' x '.join(b)}")