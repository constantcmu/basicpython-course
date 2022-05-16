from matplotlib.pyplot import cla


class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age 
        self.gender = gender

    def study(self):
        print(f'{self.name}  กำลัวเรียนอยู่.....')

    def sawatdee(self):
        if self.gender == 'ชาย':
            tail = 'ครับ'
            callme = 'ผม'
        else:
            tail = 'ค่ะ'
            callme = 'หนู'
        print(f'สวัสดี{tail}{callme} ชื่อ{self.name}')     


class SpecialStudent(Student):

    def __init__(self, name, age, gender,parent):
        super().__init__(name, age, gender)
        self.parent = parent

    def hello(self,person = 'เพื่อน'):
        if person == 'เพื่อน':
            print('ว่าไงเพื่อ')
        else:
            print('ไม่คุย')

    def sawatdee(self):
        print(f'หวัดดี ชื่อ{self.name}')

    def myfather(self):
        print('รู้ไหมกูลูกใคร')
        print(f'กูลูก {self.parent}')
        
    

class Teacher:
    def __init__(self,name , gender , subject):
        self.name = name 
        self.gender = gender
        self.subject = subject

    def teach(self):
        print('คุณครู {} กำลังสอนวิชาย {}'.format(self.name,self.subject))

    
if __name__ == '__main__':
    Student1 = Student('สมชาย',14 ,'ชาย')
    Student2 = Student('สมหญิง',15 ,'หญิง')
    Special_Student = SpecialStudent('จ้อย',18,'ชาย','นายก อบต')
    
    teacher1 = Teacher('จอห์น','ชาย' ,'ภาษาอังกฤษ')
    print(teacher1.name)
    print(teacher1.subject)

    print("---8.30---")
    Student1.sawatdee()
    Student2.sawatdee()
    teacher1.teach()
    Student1.study()
    Student2.study()

    print("---8.45---")
    Special_Student.sawatdee()
    print('เดิมไปที่โต๊ะตัวเอง')
    Special_Student.hello()
    print(f'ครู{teacher1.name}! ขอเกรดดีๆหน่อย')
    Special_Student.myfather()

