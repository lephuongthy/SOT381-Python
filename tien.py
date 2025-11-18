def tinh_so_luong_menh_gia(so_tien):
    menh_gia = [500000, 200000, 100000, 50000, 20000,
        10000, 5000, 2000, 1000, 500, 200, 100 ]
    
    print(f"Phân tách số tiền: {so_tien:,.0f} VNĐ")

    for mg in menh_gia:
        if so_tien >= mg:
            so_luong = so_tien // mg
            so_tien %= mg
            print(f"Mệnh giá {mg:,.0f} VNĐ: {so_luong} tờ/đồng.")

    if so_tien > 0:
        print(f"Còn dư {so_tien:,.0f} VNĐ không thể phân tách với các mệnh giá đã cho.")
try:
    a = int(input("Nhập vào tổng số tiền (VNĐ): "))
    
    if a < 0:
        print("Số tiền phải là một số dương.")
    else:
        tinh_so_luong_menh_gia(a)

except ValueError:
    print("Lỗi: Vui lòng nhập vào một số nguyên hợp lệ.")