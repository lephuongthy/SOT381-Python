from math import sqrt, pow
a=float(input("nhập tọa độ x của tâm O: "))
b=float(input("nhập tọa độ y của tâm O: "))
c=float(input("nhập tọa độ x của điểm M: "))
d=float(input("nhập tọa độ y của điểm M: "))
R=float(input("nhập bán kính R: "))
D=sqrt(pow((c-a),2)+pow((d-b),2))
if D>R:
    print("điểm M nằm trong hình tròn")
elif d==R:
    print("điểm M nằm trên đường tròn")
else:
    print("điểm M nằm ngoài hình tròn")



