m = int(input("nhap so nguyen duong m: "))
n = int(input("nhap so nguyen duong n: "))
tong_chu_so_n = 0
for chu in str(n):
    tong_chu_so_n += int(chu)
if tong_chu_so_n % n == 0:
    print("tong chu so cua n bang 0, khong chia duoc")
else:
    if m % tong_chu_so_n == 0:
        print("m chia het cho tong chu so cua n")
    else:
        print("m khong chia het cho tong chu so cua n")