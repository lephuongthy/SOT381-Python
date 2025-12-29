a=float(input("nhập điểm môn toán: "))
b=float(input("nhập điểm môn lý: "))
c=float(input("nhập điểm môn hóa: "))
if (a+b+c)>=15 and (a>4 and b>4 and c>4):
    print(f"thi đậu")
    if a>5 and b>5 and c>5:
        print(f"học đều")
    else:
        print(f"học chưa đều các môn")
else:
    print(f"thi hỏng")