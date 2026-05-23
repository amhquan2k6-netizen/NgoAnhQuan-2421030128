#Bài 3: Viết chương trình nhập vào 2 số nguyên dương a và b, sau đó kiểm tra xem a có chia hết cho chữ số nhỏ nhất của b hay không
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
nho_nhat = 9
b2 = b
while b2 > 0:
    cs = b2 % 10
    if cs < nho_nhat:
        nho_nhat = cs
    b2 = b2 // 10
if nho_nhat != 0:
    if a % nho_nhat == 0:
        print('Chia hết')
    else:
        print('Không chia hết')
else:
    print('Chữ số nhỏ nhất là 0, không thể chia')