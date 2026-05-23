m = int(input('Nhập m: '))
n = int(input('Nhập n: '))
tong = m + n
lon_nhat = 0
t = tong
while t > 0:
    cs = t % 10
    if cs > lon_nhat:
        lon_nhat = cs
    t = t // 10
print('Tổng = ', tong)
print('Chữ số lớn nhất trong tổng là: ', lon_nhat)