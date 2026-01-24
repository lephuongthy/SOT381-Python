from decimal import getcontext 
a=input("nhap loai xe: ")
b=float(input("nhap so gio"))
"""Nếu là “xe_may”: 5.000đ cho 2 giờ đầu. Mỗi giờ tiếp theo là 2.000đ.
Nếu là “o_to”: 20.000đ cho giờ đầu tiên. Mỗi giờ tiếp theo là 15.000đ."""
if a in ("xe may", "oto"):
    getcontext().prec=2
    if a=="xe may":
        if b<=2:
         print(f"tien do xe la {b*5000}")
        else:
           print(f"tien do xe la {10000+(b-2)*2000}")
    if a=="oto":
        if b<=1:
          print(f"tien do xe la {b*20000}")
        else:
          print(f"tien do xe la {20000+(b-1)*15000}")