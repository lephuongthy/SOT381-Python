'''bậc 1: 50 kWh đầu tiên (0-50 kWh): 1.984 VND/kWh
   bậc 2: 50 kWh tiếp theo (51-100 kWh):  2.050 VND/kWh
   bậc 3: 100 kWh tiếp theo (101-200 kWh):  2.380 VND/kWh
   bậc 4:  kWh còn lại (201-... kWh ): 2.998 VND/kWh
'''
a=int(input("nhap so khoi dien cua ban: "))
if a>0:
    if a<=50:
        print(f"tong tien dien cua ban la: {a*1.984}")
    elif 50<a<=100:
        print(f"tong tien dien cua ban la: {(50*1.984)+(a-50)*2.050}")
    elif 100<a<=200:
        print(f"tong tien dien cua ban la: {(50*1.984)+(50*2.050)+(a-100)*2.380}")
    else:
        print(f"tong tien dien cua ban la: {(50*1.984)+(50*2.050)+(100*2.380)+(a-200)*2.998}")