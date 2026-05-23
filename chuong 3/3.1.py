#Nhập vào 1 số n. Hãy viết hàm tính giai thừa của n đó
n = int(input("Nhap n: "))
def giaithua(m):
    gt = 1
    for i in range(1, m+1):
        gt = gt + i
    return gt
n = int(input("Nhap vao 1 so nguyen duong:"))
print("%d != %d" %(n, giaithua(n)))