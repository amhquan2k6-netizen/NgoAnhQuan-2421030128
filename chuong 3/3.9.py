#Chương trình cho phép nhập vào 1 dãy số nguyên gồm n phần tử. Ghi dãy số vừa nhập ra tệp "dulieu.txt" ở ổ đĩa C"\
a = []
n = int(input("Nhap so phan tu cua day so: "))
for i in range(1, n+1):
    k = int(input("Nhap phan tu thu" + str(i) + ":"))
    a.append(k)
obj = open("C:\dulieu.txt", "w")
for i in a:
    obj.write(str(i) + " ")
obj.close()