n = int(input("nhap so nguyen duong n: "))
tich = 1
for chu in str(n):
    tich = tich * int(chu)

if tich % 2 == 0 and tich > 20:
    print("tich la so chan va lon hon 20")
else:
    print("khong thoa man dieu kien")