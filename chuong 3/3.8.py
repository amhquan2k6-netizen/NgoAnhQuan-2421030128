#Tạo 1 file có abcd.txt và ghi ra file dòng chữ "Python xin chao cac ban"
obj = open("abcd.txt", "w")
obj.write("Python xin chao cac ban")
obj.close()