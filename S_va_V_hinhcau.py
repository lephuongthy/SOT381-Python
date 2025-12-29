#nhập vào bán kính hình cầu và in ra diện tích, thể tích
from math import pi, pow
r=float(input("nhập vào bán kính hình cầu: "))
print(f"diện tích hình cầu là S={4*pi*pow(r,2):.2f}")
print(f"thể tích hình cầu là V={(4/3)*pi*pow(r,3):.2f}")