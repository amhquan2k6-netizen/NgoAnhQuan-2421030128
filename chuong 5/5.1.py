class Circle:
    def Dientich(self):
        return self.bk*self.bk*3.141592
    def Nhap(self):
        self.bk = float(input("Nhap ban kinh: "))
c = Circle()
c.Nhap()
print("Dien tich cua hinh tron la: ", c.Dientich())