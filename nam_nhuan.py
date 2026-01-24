x=int(input("nhập một năm bất kì: "))
if (x%4==0 and x%100!=0) or (x%400==0):
    print(f"năm {x} là năm nhuận")
else:
    print(f"năm {x} không phải năm nhuận") 