n = int(input("nhap so nguyen duong n: "))

tong_chu_so = 0 
for chu in str(n):
    tong_chu_so += int(chu)

if tong_chu_so % 3 == 0:
    print("tong chia het cho 3")
else:
    print("tong khong chia het cho 3")