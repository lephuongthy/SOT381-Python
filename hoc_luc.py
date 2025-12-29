a=float(input("nhập điểm trung bình của bạn: "))
if a>0 and a<=10:
    if a>8 or a==8:
       print(f"học lực giỏi")
    elif a>6.5 or a==6.5:
       print(f"học lực khá")
    elif a>5 or a==5:
       print(f"học lực trung bình")
    elif a>3.5 or a==3.5:
       print(f"học lực yếu")
    else:
       print("học lực kém")
else:
   print("điểm không hợp lệ")