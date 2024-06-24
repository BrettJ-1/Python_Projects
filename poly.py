class User:
    name = "Brett"
    email = "brettj@gmail.com"
    password = "Brett_J"

    # As a customer, I (personal) will recieve a request for an email and password to login. 
    
def getLoginInfo (personal) :
    entry_name = input ("Enter your name: ")
    entry_email = input ("Enter your email: ")
    entry_password = input ("Enter you password: ")
    if (entry_email == personal.email and entry_password = personal.password) :
        print ("Welcome back, (}!". format(entry_name))
    else:
        print ("The password or email is incorrect.")

        #Manager will recieve a pin_number activation instead of entry_password.
        
class Employee (User) :
    base_pay = 16.75
    department = "Hardware"
    pin_number = "7207"

    def getLoginInfo(personal):
        entry_name = input ("Enter your name: ")
        entry_email = input ("Enter your email: ")
        entry_pin = input ("Enter your Personal Identification Number: ")
        if (entry_email = personal.email and entry_pin = personal.pin_number) :
            print ("Nice to see you again, ()!". format(entry_name))
else:
print ("The pin or email is incorrect, please try again!")
customer = User ()
customer.getLoginInfo ()

manager = Employee ()
manager.getLoginInfo ()
