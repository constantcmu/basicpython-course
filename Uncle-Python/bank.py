class BankAccount:
    def __init__(self,name,age,amount):
        self.name = name 
        self._age = age         #สืบท้องเฉพาะ class
        self.__amount = amount  #สืบท้อง private

    def showMessage(self):
        print('กำลังทำรายการฝาก-ถอนเงินในบัญชี')

    def _deposit(self,deposit):
        self.__amount += deposit
        print(f'ฝากเพิ่ง {deposit} รวมเงิน {self.__amount}')
    
    def getAmout(self):
        return self.__amount

    def setAmount(self,amount):
        self.__amount = amount
        
    def __withdraw(self,withdraw):
        self.__amount -= withdraw
        print(f'ถอนเงิน {withdraw} เหลือเงิน {self.__amount}')
    
    data = property(getAmout,setAmount)


class Employee(BankAccount):
    def __init__(self, name, age, amount):
        super().__init__(name, age, amount)

if __name__ == '__main__':
    employee = Employee('Nattawut',30,10000)
    print(employee.name)
    print(employee._age)
    print(employee.data)
    
    employee.data = 200000
    print(employee.data)
    # employee.showMessage()
    # employee._deposit(5000)
    # employee.__withdraw(300)