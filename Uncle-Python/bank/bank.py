class BankAccount:

    no_of_cust = 0      #จำนวน บช
    acc_num = 0         #เลขบัญชี

    def __init__(self, name , mobile_no , initial_depo , pin):
       self.name            = name 
       self.cust_acc_num    = BankAccount.acc_num   #เลขบัญชีใหม่
       self.mobile_no       = mobile_no             #เลขโทรศัพท์
       self.acc_balance     = initial_depo          #กำหนดยอดใน บช = ยอดแรกเข้า
       self.pin             = pin                   #รหัส

       BankAccount.acc_num  += 1    #เพิ่มจำนวน บช
       BankAccount.no_of_cust += 1

    def basic_details(self):  
        print(f'User : {self.name}\t Account No: {self.cust_acc_num}\t Balance : ฿{self.acc_balance}')

    def deposit(self):
        amount = int(input('จำนวนเงินที่ต้องการฝาก : '))
        if amount > 0 :
            self.acc_balance += amount
            print(f'ธุรกรรมเสร็จสมบูรณ์ ยอดเงินปัจจุบัน :฿{self.acc_balance}')
        else:
            print('ธุรกรรมจำนวนเงินที่ไม่ถูกต้องถูกยกเลิก')
    
    def withdrawl(self):
        amount = int(input('จำนวนเงินที่ต้องการถอน : '))
        if amount <= self.acc_balance and amount > 0 :
            self.acc_balance -= amount 
            print(f'ธุรกรรมเสร็จสมบูรณ์ ยอดเงินปัจจุบัน :฿{self.acc_balance}')
        else:
            print('ธุรกรรมจำนวนเงินที่ไม่ถูกต้องถูกยกเลิก')

    def payment(self,other):  #การโอนเงิน
        amount = int(input('ใส่จำนวนเงินที่ชำระ : '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance -= amount
            other.acc_balance  += amount
            print(f'ธุรกรรมเสร็จสมบูรณ์ ยอดเงินปัจจุบัน :฿{self.acc_balance}')
        else:
            print('ธุรกรรมจำนวนเงินที่ไม่ถูกต้องถูกยกเลิก')

if __name__ == '__main__':
    #test 
    cust1 = BankAccount(name='สมคิด', mobile_no=9876543210, initial_depo=1000, pin=123)
    cust2 = BankAccount(name='สมหญิง', mobile_no=9876543212, initial_depo=2000, pin=456)
    print('No. of customers is',BankAccount.no_of_cust)
    print(cust1.basic_details())
    print(cust2.basic_details())
    cust1.deposit()
    print(cust1.basic_details())
    cust1.withdrawl()
    print(cust1.basic_details())
    cust1.payment(cust2)
    print(cust2.basic_details())           
        
        
