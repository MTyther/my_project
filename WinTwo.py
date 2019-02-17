def login(myName, myID):
    balance = "$100.00"
    if myName == "Martin" and myID == "1234":
        print("Welcome, " + myName)
        print("Your current balance is: " + balance)
    else:
        print("Invalid entry, Please re-enter correct Name and/or ID: ")


m_Name = input("Please enter your first name: ")
m_ID = input("Enter your ID#: ")
login(m_Name, m_ID)