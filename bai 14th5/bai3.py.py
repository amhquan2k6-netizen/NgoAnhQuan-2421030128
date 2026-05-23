#Viết chương trình nhập vào 1 dãy số x1, x2,... xn (0 < n < 100), sau đó tìm trung bình cộng các phần tử âm trong dãy mà giá trị nằm trong khoảng (-1000, -10)
n = int(input("Nhap n = "))
tong = 0
dem = 0
for i in range(n):
    x = float(input("Nhập số phần tử: "))
    if -1000 < x < -10:
        tong += x
        dem += 1
if dem > 0:
    print("Trung bình cộng: ", tong/dem)
else:
    print("Không có phần tử phù hợp")