a = int(input("nhap so nguyen duong a: "))
b = int(input("nhap so nguyen duong b: "))
tong = a + b
print("tong cua a va b la: ", tong)
chu_so_lon_nhat = 0
for chu in str(tong):
    if int(chu) > chu_so_lon_nhat:
        chu_so_lon_nhat = int(chu)
print("chu so lon nhat trong tong la: ", chu_so_lon_nhat)