# giải phương trình bậc 1 ax+b=0
a=float(input("nhập hệ số a: "))
b=float(input("nhập hệ số b: "))
if a==0:
     if b==0:
            print(f"phuong trinh co vo so ngiem")
     else:
            print(f"phuong trinh vo nghiem")
else:
        print(f"phuong trinh co nghiem x={-b/a}")
