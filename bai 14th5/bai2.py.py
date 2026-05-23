#Viết chương trình nhập vào 1 dãy số nguyên x1, x2,...,xn (0 < n < 200). Tính tổng các phần tử chẵn trong dãy và kiểm tra xem tổng này có chia hết cho 7 và nhỏ hơn 200 hay không?
n = int(input("Nhap n = "))
if 0 < n < 200:
    tong = 0
    for i in range(n):
        x = int(input(f"Nhap x[{i}] = "))
        if x % 2 == 0:
            tong += x
    print("Tong chan =", tong)
    if tong % 7 == 0 and tong < 200:
        print("Thoa man")
    else:
        print("Khong thoa man")
else:
    print("n khong hop le!")