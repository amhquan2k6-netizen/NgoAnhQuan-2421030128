#Viết chương trình nhập vào 2 số nguyên dương a và b, sau đó kiểm tra xem a có chia hết cho chữ số nhỏ nhất của b hay không
a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
min_digit = 9
for i in str(b):
    if int(i) < min_digit:
        min_digit = int(i)
print("Chu so nho nhat cua b la:", min_digit)
if min_digit != 0 and a % min_digit == 0:
    print(a, "chia het cho", min_digit)
else:
    print(a, "khong chia het cho", min_digit)