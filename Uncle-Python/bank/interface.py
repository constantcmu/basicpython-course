from bank import BankAccount

customer_dict = {}          #ใช้เลขที่บัญชี เป็นkey และคลาสอ็อบเจ็กต์ (บัญชีลูกค้า) value
mobile_acc_link = {}        #ใช้เบอร์มือถือ เป็นkey และเลขที่บัญชีของร้าน เป็น value เพื่อเชื่อมโยง

def new_cust():
    name = input(' กรุณากรอกชื่อเจ้าจองบัญชี :  ')
    mobile_no = int(input('กรุรารกรอกหมายเลขโทรศัพท์ :  '))
    intial_depo = int(input('จำนวนเงินที่ต้องการฝาก : '))

    if intial_depo <= 0:
        print('จำนวนเงินที่ไม่ถูกต้อง')
        return

    pin = int(input('สร้างรหัสเข้าธุรกรรม : '))
    customer = BankAccount(name=name,mobile_no=mobile_no,initial_depo=intial_depo,pin=pin)
    customer_dict[customer.cust_acc_num] = customer                 # acct. no. stored as key and oject as value
    mobile_acc_link[customer.mobile_no] = customer.cust_acc_num     # mobile no. linked

    print('สร้างบัญชีสำเร็จ!')
    print(f'ขอบคุณ {customer.name} ที่ใช้บริการธนาคาร {customer.cust_acc_num} เป็นหมายเลข บัญชีของคุณ ')

def login():
    account_no = int(input('กรอกหมายเลชบัญชีของคุณ : '))
    account_pin = int(input('กรอกรหัสผ่านบัญชีของคุณ : '))
    if account_no in customer_dict.keys() and account_pin == customer_dict[account_no].pin :
        print(f'\n{customer_dict[account_no].name} Logged in ')
        customer_dict[account_no].basic_details()
    else:
        print('ไม่มีเลขบัญชีนี้อยู่หรือพินผิด')
        return
    while True:
        user_input1 = input(''' กดหมายเลข  1 ฝากเงิน : 
        กดหมายเลข  2 ถอนเงิน
        กดหมายเลข  3 โอนเงิน
        กดหมายเลข  4 ออกจากระบบ''')
        if user_input1 == '1':
            customer_dict[account_no].deposit()
        elif user_input1 == '2':
            customer_dict[account_no].withdrawl()
        elif user_input1 == '3':
            mobile = int(input('ป้อนหมายเลขโทรศัพท์มือถือของผู้รับ : '))
            if mobile in mobile_acc_link.keys():
                secondary = mobile_acc_link[mobile]                         #ใช้เบอร์มือถือ เพื่อรับบัญชี เลข บช
                customer_dict[account_no].payment(customer_dict[secondary])
            else:
                print('หมายเลขโทรศัพท์มือถือที่คุณป้อนไม่มีบัญชีที่เชื่อมโยงอยู่')

        elif user_input1 == '4':
            print('ออกจากระบบแล้ว')
            return
        else:
            print('กรอกข้อมูลไท่ถูกต้อง โปรดลองใหม่')
        print('\n##########################################################################################\n')
        customer_dict[account_no].basic_details()


while True:
    user_input1 = input('''กด 1 สร้างบัญชีใหม่:
กด 2 เข้าสู่ระบบในฐานะลูกค้าปัจจุบัน:
Press 3 เพื่อแสดงจำนวนลูกค้า:
Press 4 ออกจากระบบ\n''')

    if user_input1 == '1':
        print('สร้างบัญชีผู้ใช้')
        new_cust()
    elif user_input1 == '2':
        login()
    elif user_input1 == '3':
        print('ขณะนี้มีจำนวน', BankAccount.no_of_cust,'หมายเลขบัญชี')
    elif user_input1 == '4':
        print('ออกจากระบบแล้ว')
        break
    else:
        print('การป้อนข้อมูลไม่ถูกต้อง ลองอีกครั้ง')
    print('\n*************************************************************\n')


        


