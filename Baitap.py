def tach_du_lieu():
        with open("input.txt", "r", encoding="utf-8") as f_in:
            noi_dung = f_in.read()
        chuoi_so = ""
        chuoi_chu = ""
        for char in noi_dung:
            if char.isdigit():      
                chuoi_so += char
            elif char.isalpha():    
                chuoi_chu += char
            elif char.isspace():    
                chuoi_so += char
                chuoi_chu += char
        with open("outso.txt", "w", encoding="utf-8") as f_so:
            f_so.write(chuoi_so.strip())
        with open("outchu.txt", "w", encoding="utf-8") as f_chu:
            f_chu.write(chuoi_chu.strip())
        print("Đã tách dữ liệu thành công!")
        print("Lỗi: Không tìm thấy file input.txt")
if __name__ == "__main__":
    tach_du_lieu()
    s = 0
n = int(input("nhap so phan tu cua day so:"))
for 1 in range(1, n + 1):
    k = int(input("nhap phan tu"+ str(i)+""))
    for i in a:
        print("tong cua day so la:"+ str(s))
#phuong trinh cho phep nhap vao ma tran gom m hang,n cot......
m = int(input("Nhap m="))
n = int(input("Nhap n="))
a = []
for i in range (0,m):
    a.append([])
    for j in range (0,n):
        x = float(input("Nhap phan tu a[%d][$d]:"%(i + 1,j + 1)))
a [i].append(x)
print("many vua nhap la:")
for i in range (0,m):
    for j in range (0,n):
        print("%8.2",a[i][j],end='')
        print()
#vd viet pt hien sau 1 ki tu.....
ss = "CNTT"
index = 0
while index < len(s):
    letter = s[index]
    print(letter)
    index = index + 1
#vd 5 nhap vao 1 so kiem tra xem so do co phai hoan hao ko .....
n = int(input("n="))
s = 0
for i in range (1,n):
    if n %i == 0:
        s = s + i
        if s == n:
            print(n,"n la so hoan hao")
        else:
            print(n,"n khong la so hoan hao")
#vd6 tim so hoan hao.....
s = int(input("Nhap gioi han: "))
for n in range(1, s + 1):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong = tong + i
    if tong == n:
        print(n)
#vd....
n = int (input("nhap vao 1 so nguyen:"))
if ('n% 2 == '):
    print("so" + repr(n) + "la so chan")
else:
    print("so" + repr(n) + "la so le")
#vd ax + b = 0.....
a = float(input("nhap he so a="))
b = float(input("nhap he so b="))
if(a==0):
 if(b==0):
    print("phuong trinh vo so nhiem")
else:
    print("phuong trinh vo so nhiem")
X = -a/b 
print("x =",x)   