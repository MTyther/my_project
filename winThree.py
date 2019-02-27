import random

def menu():
    print("\n")
    print("******** MENU ********")
    print("----------------------")
    print(" A - Add New Customer ")
    print(" U - Update Customer  ")
    print(" D - Delete Customer  ")
    print(" Q - Quit             ")
    print("======================")
    
def append_record(cust, fname, lname, caddress, ccity, cstate, czip):
   new_record.append(cust)
   #new_record.append(customer_id)
   new_record.append(fname)
   new_record.append(lname)
   new_record.append(caddress)
   new_record.append(ccity)
   new_record.append(cstate)
   new_record.append(czip)
   write_record(new_record)

def write_record(new_rec):
    try:
       with open("C:\\...\\datafile.txt", "w") as f:
           f.write(str(new_rec))
           print("\n")
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def read_record():
    try:
       with open("C:\\...\\datafile.txt", "r") as f:
           print(f.read())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def new_customer():
    customers = 0
    print("Adding New Customer!")
    while True:
        f_name = input("Your firstname? ")
        if len(f_name) > 0:
            l_name = input("Your lastname? ")
            if len(l_name) > 0:
                c_address = input("Address? ")
                if len(c_address) > 0:
                    c_city = input("City? ")
                    if len(c_city) > 0:
                        c_state = input("State? ")
                        if len(c_state) > 0:
                            c_zip = input("Zip code? ")
                            if len(c_zip) > 0:
                                customers += 1
                                append_record(customers, f_name, l_name, c_address, c_city, c_state, c_zip)
                                read_record()
        else:
            print("You must make a valid entry!") 
            break

new_record = []
       
while True:
    menu()
    selection = input("Choose from the menu:")
    if selection == "A" or selection == "a":
        new_customer()
    elif selection.upper() == "U":
        print("Updating customer record!")
    elif selection.upper() == "D":
        remove = input("Delete customer(Y/N)? ")
        if remove.upper() == "Y":
            print("Sorry to see you go, deleting record!")
            #replace break with function call
            #to remove customer information from file.
            continue
    elif selection.upper() == "Q":
        print("Good Bye!")
        break
    else:
        print("Choose an option from the menu!")
        continue        
          
  
