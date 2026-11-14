import getpass  # Mandatory built-in module for hiding password text input

class User:
    name = ''
    email = ''
    password = ''
    is_authenticated = False

    def setup_account(self):
        self.name = input("Set account name: ")
        
        # Enforcing strict email syntax via an infinite validation loop
        while True:
            test_email = input("Set registration email (Must be @gmail.com): ")
            if test_email.endswith("@gmail.com"):
                self.email = test_email
                break
            print("❌ Invalid Email! You must register using a @gmail.com address.")
            
        # Securing password registration using text masking
        self.password = getpass.getpass("Set account password (Hidden): ")
        print("Registration completed successfully!\n")

    def authenticate_user(self):
        print(f"--- Login Portal for {self.name} ---")
        input_email = input("Enter email: ")
        
        # Securing password entry on authentication stage
        input_password = getpass.getpass("Enter password (Hidden): ")
        
        if input_email == self.email and input_password == self.password:
            self.is_authenticated = True
            print("Login successful!")
        else: 
            print("Failed: Invalid email or password")
            
    def display_profile(self):
        if self.is_authenticated:
            print(f"\n--- User Profile ---\nName: {self.name}\nEmail: {self.email}")
        else: 
            print("\nAccess Denied: User session is unauthorized!")

# Execution testing flow
user1 = User()

# 1. Setup account variables with secure inputs
user1.setup_account()

# 2. Test user login verification loop
user1.authenticate_user()

# 3. Request confidential data profile block
user1.display_profile()
