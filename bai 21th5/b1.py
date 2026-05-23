n = int(input("nhap so luong phan tu: "))
day_so = []
for i in range(n):
    x = float(input("nhap so thu {i+1}: "))
    day_so.append(x)
tong = 0 
dem = 0
for so in day_so:
    if 0 < so < 1000:
        tong += so
        dem += 1    
if dem > 0:
    trung_binh = tong / dem
    print("trung binh cong = {trung_binh:.2f}")
else:
    print("khong co so nao trong khoang (0, 1000)")