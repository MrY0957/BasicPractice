class User:
#class Attributes/properties
    name = ''
    email = ''
    password = ''
    is_authenticated = False

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    def user_login(self):
        input_email = input("Enter email: ")
        input_password = input("Enter password: ")
        #check valid
        if input_email == self.email and input_password == self.password:
            self.is_authenticated = True
            print("Login successful!")
        else: 
            print("Faild: Invalid Input")
    def logout(self):
        self.is_authenticated = False #Properly resetting object state via self
        print("Logged Out!")
    
    def check_loggedIn(self):
        return self.is_authenticated
    
    def profile(self):
        # Enforcing access authorization check to solve security bug
        if self.check_loggedIn():
            print(f" User Profile \nName: {self.name}\nEmail: {self.email}")
        else: 
            print("Access Denied: User is not Logged in!")
## Execution testing flow to create object and test run
user1 = User()
# Simulating login workflow
user1.user_login()
user1.profile()
