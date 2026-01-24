def tinh_so_luong_menh_gia(so_tien):
    menh_gia = [500000, 200000, 100000, 50000, 20000,
        10000, 5000, 2000, 1000, 500, 200, 100 ]
    
    print(f"phan tach so tien: {so_tien:,.0f} VNĐ")

    for mg in menh_gia:
        if so_tien >= mg:
            so_luong = so_tien // mg
            so_tien %= mg
            print(f"menh gia {mg:,.0f} VNĐ: {so_luong} to/dong.")

    if so_tien > 0:
        print(f"con du {so_tien:,.0f} VNĐ khong the phan tach voi cac menh gia da cho.")
try:
    a = int(input("nhap vao tong so tien (VNĐ): "))
    
    if a < 0:
        print("so tien phai la so duong.")
    else:
        tinh_so_luong_menh_gia(a)

except ValueError:
    print("vui long nhap lai so tien.")