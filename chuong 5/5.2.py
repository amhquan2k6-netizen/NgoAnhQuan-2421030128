class Circle:
    pi = 3.141592
    def __init__ (self, radius = 1):
        self.bk = radius
    def Dientich(self):
        return self.bk*self.bk*Circle.pi
c = Circle(5)
print("Dien tich cua hinh tron la: ", c.Dientich())