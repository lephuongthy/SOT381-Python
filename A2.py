#tính S=1/1*2 + 1/2*3+..+1/n*(n+1)
n=int(input("nhập giới hạn n: "))
S=0
if n<=0:
    print("số n không hợp lệ")
else:
    for i in range(1,n+1):
        S+=1/(i*(i+1))

print("tổng S=1/1*2 + 1/2*3+..+1/n*(n+1) là:")
print(S)