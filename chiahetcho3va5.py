#in ra các số từ 1 đến 100 chia hết cho 3 và 5
i=1
a=[]
while i<=100:
    if i%3==0 and i%5==0:
        a.append(i)
    i+=1
print(f"các số từ 1 đến 100 chia hết cho 3 và 5 là:")
print(a)
