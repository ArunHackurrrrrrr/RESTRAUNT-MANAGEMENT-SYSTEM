import ast
from datetime import datetime

# dict = {}

def main_screen():
    print('WELCOME TO OUR SOFTWARE \n WE HAVE FOLLOWING OPTIONS YOU CAN USE \n (1) MENU MANGAEMENT \n (2) STAFF MANAGEMENT \n (3) BILLING SYSTEM \n (4) TABLE BOOKING \n (5) ORDER MANAGEMENT \n (6) INVENTORY MANGAEMENT \n (7) QUIT ')
    userInp = int(input('ENTER YOUR CHOICE : \n'))
    
    if userInp==1:
        menuManage()
    elif userInp ==2:
        staffManage()
    elif userInp ==3:
        billingSys()
    elif userInp ==4:
        tableBook()
    elif userInp ==5:
        orderManage()
    elif userInp ==6:
        inventManage()
    elif userInp ==7:
        quit()
    else:
        print("PLEASE MAKE SURE TO ENTER CORRECT INPUT ")
        main_screen()

def dictMaker(fileName):
    with open(f'{fileName}.txt','r') as dictData:
        dictReadData = dictData.read().strip()
        dictReadData2 = f"({dictReadData})"
        convOne = dictReadData2.replace("(","{")
        convTwo = convOne.replace(")","}")
        dictReadDataConv = ast.literal_eval(convTwo)
        print(dictReadDataConv.keys())
        return dictReadDataConv
    

def readingWriting(fileName,data,modeo):
    print(data)
    with open(f'{fileName}.txt', f'{modeo}') as readWrite:
        readWrite.write(f'{data} \n')


def menuManage():
    print('work')
    print("(1) IF YOU WANT TO ADD DISH ON MENU (2) IF YOU WANT TO EDIT A DISH ON MENU")
    userInp = int(input('ENTER YOUR CHOICE'))

    if userInp == 1:
        dishName = input("ENTER THE NAME OF THE DISH")
        dishPrice = input("ENTER THE PRICE OF THE DISH")
        dishServing = input("ENTER THE SERVING PRICE OF THE DISH")
        dishManPrice = input("ENTER THE MANUFACTURING PRICE OF THE DISH")

        dishData = f"'{dishName}' : ( \n'Price' : '{dishPrice}',\n'Cost' : '{dishManPrice}',\n'Serving size' : '{dishServing}' )"

        dishnew = dishData.replace('(','{')
        dishnew2 = dishnew
        dishnew3 = dishnew2.replace(')','}')
        print(dishnew3)

        readingWriting('Menu',f'{dishnew3}')

def staffManage():
    print('(1) FOR ATTENDENCE OF STAFF \n(2) TO ADD A STAFF MEMBER \n(3) TO DELETE RECORD OF A MEMBER')
    userInp = int(input("ENTER YOUR CHOICE"))
    if userInp == 1:
        storData = dictMaker('STAFF')
        print(storData)
        AttName = list(storData.keys())
        print('ye hai attname')
        print(AttName)
        date = datetime.now()
        formatted_date = date.strftime("%d-%m-%Y")
        print(formatted_date)
        for noAtt in range (0,len(AttName)):
            print(f'({noAtt + 1}) {AttName[noAtt]}')
        userInpAtt = (input('ENTER THE NO FOR ATTENDENCE in series : '))
        userInpAttLis = (userInpAtt)
        for no in userInpAttLis:
            print(no)
            no = int(no)
            attData = f"{formatted_date} ----> {AttName[no -1]}"
            print(f' yaha hai {attData}')
            readingWriting('ATTENDENCE',attData,'a')
            
        
        
        
    
    if userInp == 2 :
        userInpName = input('ENTER THE NAME OF NEW STAFF')
        userInpCont = input('ENTER THE CONTACT NO OF STAFF')
        userInpPost = input('ENTER THE ROLE OF NEW STAFF MEMBER')
        StaffData = f"'{userInpName}' : ( \n'Contact' : '{userInpCont}',\n'Post' : '{userInpPost}' ),"
        
        StaffData = StaffData.replace('(','{')
        StaffData2 = StaffData
        staffdata3 = StaffData2.replace(')','}')
        print(staffdata3)

        readingWriting('STAFF',staffdata3,'a')
    
    if userInp == 3:
        staffRecord = dictMaker('STAFF')
        staffRecordLis = (staffRecord)
        print(staffRecordLis)
        userInpDelDataName = input('ENTER THE NAME OF THE MEMBER YOU WANT TO REMOVE : ')
        # newStaff = staffRecord.pop(userInpDelDataName)
        # newStaff = del staffRecord [f'userInpDelDataName']
        del staffRecord [f'{userInpDelDataName}']
        # newStaffRecord = f'({staffRecord})'

        newStaffRecordStr = f'{staffRecord}'
        print('ye hai len')
        print(len(newStaffRecordStr))
        # newStaffRecordStr2 = newStaffRecordStr.replace('{',' ')
        # newStaffRecordStr3 = newStaffRecordStr2.replace('}',' ')
        newStaffRecordStrData = newStaffRecordStr[:0] + newStaffRecordStr[1:]
        newStaffRecordStrData2 = newStaffRecordStrData[:len(newStaffRecordStrData)] + newStaffRecordStrData[len(newStaffRecordStrData) -1 :]
        # newStaffRecord2 = newStaffRecord.replace('(','{')
        # newStaffRecord3 = newStaffRecord2.replace(')','}')

        readingWriting('STAFF',newStaffRecordStrData2,'w')
        print('ye haih naeee')
        print(newStaffRecordStrData2)


       


def billingSys():
    pass


def tableBook():
    userInp = int(input("(1) TO BOOK A NEW BOOKING \n (2) TO ROMOVE A BOOKING "))
    if userInp == 1:
        userInpName = input('ENTER THE NAME OF CUSTOMER : ')
        userInpDate = input('Enter the date of booking')
        userInpCont = input('ENTER THE CONTACT INFORMATION')

        CustomerData = f"'{userInpName}' : ( \n'Contact' : '{userInpCont}',\n'Date' : '{userInpDate}' )"       
        CustomerData = CustomerData.replace('(','{')
        CustomerData2 = CustomerData
        CustomerData3 = CustomerData2.replace(')','}')
        print(CustomerData3)

        readingWriting('BOOKING',CustomerData3)
    if userInp ==2:
        print('working on it')



def orderManage():
    userInp = int(input('(1) TO PLACE AN ORDER FOR A TABLE \n (2) TO CANCEL AN ORDER'))

    if userInp == 1:
        userInpTableNo = input("ENTER THE TABLE YOU WANT TO TAKE ORDER")
        userInpDish = input("ENTER THE DISH no. ")
        OrderData = f"'{userInpTableNo}' : ( \n'Post' : ' {userInpDish}' )"        
        OrderData = OrderData.replace('(','{')
        OrderData2 = OrderData
        OrderData3 = OrderData2.replace(')','}')
        print(OrderData3)

        readingWriting('ORDERMANAGEMENT',OrderData3)

def inventManage():
    pass



main_screen()