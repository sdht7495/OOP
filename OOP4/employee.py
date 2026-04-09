class Nhan_vien:
    luong_max = 50000000
    def __init__(self, ten, luongCB, hesoluong):
        self.__ten = ten
        self.__luongCB = luongCB
        self.__hesoluong = hesoluong

    def getten(self):
        return self.__ten
    
    def getluong(self):
        return self.__luongCB
    
    def gethesoluong(self):
        return self.__hesoluong

    def setluongCB(self, value):
        if value < 0:
            print("khong the be hon 0")
            return
        self.__luongCB = value

    def sethesoluong(self, value):
        if value <= 0:
            print("khong the be hon hoac bang 0")
            return
        self.__hesoluong = value

    def tinhluong(self):
        return self.__luongCB * self.__hesoluong
    
    def intt(self):
        luong = self.tinhluong()
        print(f" ten nhan vien: {self.__ten}")        
        print(f" luongCB: {self.__luongCB} VND")
        print(f" he so luong: {self.__hesoluong}")
        print(f" luong nha vien: {luong} VND")

    def TangLuong(self, delta):
        he_so = self.hesoluong + delta
        luongmoi = self.luongCB * he_so

        if luongmoi > Nhan_vien.luong_max:
            print("luong moi khong duoc cao hon muc luong cao nhat")
            return False
        else :
            self.hesoluong = he_so
            print("tang luong thanh cong")
            return True