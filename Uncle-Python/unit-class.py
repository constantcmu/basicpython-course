from io import BufferedRandom


class Car():
    #Attribute
    brand = None
    year = None
    fuel = None  #%
    status = None

    #method ใช้ขึ้นต้นตังเล็ก
    #Constructor เป็นเมธอดตัวหนึ่งภายในคลาส จะทำงานโดยอัตโนมัติทันทีหลังจากสร้าง object

    def __init__(self,brand = 'Toyota',year = 2020 , fuel = 100.00 , status = True):     #run auto ที่เริ่มต้น
       self.brand = brand
       self.year = year
       self.fuel = fuel
       self.status = status

    def checkstatus(self):
        if self.status == True:
            print('รถยนต์คนนี้ ผ่านการทดสอบ')
        else:
            print('รถยนต์คนนี้ยังไม่ผ่าน')

    def drive(self):
        print('a car is driving')

if __name__ == '__main__':
    car01 = Car()
    car01 = Car('Benz',2020,20.00,True)   #object1
    car02 = Car('Honda',2022,40.00 ,False   )   #object2
    print(f'ยี่ห้อ : {car01.brand}')    #เรียกใช้งานตัวแปร
    print(f'ปีที่ผลิต :{car01.year}')   
    print(f'ระดับเชื้อเพลิง :{car01.fuel}')

    car01.checkstatus()     #เรียกใช้งานฟังก์ชั่น
    car01.drive()           #run auto ที่ init ของ Car()  #เรียกใช้งานฟังก์ชั่น
    car02.checkstatus()     #เรียกใช้งานฟังก์ชั่น