#tính tổng S=1+3+5+..+(2n+1)
n=int(input("nhập giới hạn n: "))
S=0
for i in range(0,n+1):
    S+=2*i+1

print("tổng S=1+3+5+..+(2n+1) là: ")
print(S)
      