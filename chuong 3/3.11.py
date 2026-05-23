#Đọc và in ra nội dung của tệp abcd.txt đã được tạo ở vd10
obj1 = open("abcd.txt", "r")
s1 = obj1.read()
print(s1)
obj1.close()

obj2 = open("abcd.txt", "r")
s2 = obj2.read(6)
print(s2)
obj2.close()