import sys
import os

# Helper utility to read a single raw character from the terminal across platforms
def read_char():
    if os.name == 'nt':  # Windows configuration
        import msvcrt
        ch = msvcrt.getch()
        # Decode special character streams cleanly
        if ch in (b'\x00', b'\xe0'):
            msvcrt.getch()  # Clear arrow keys and function shortcuts
            return ''
        return ch.decode('utf-8', errors='ignore')
    else:  # Unix / macOS configuration
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

# Custom dynamic input engine built for character control
def secure_email_input(prompt):
    print(prompt, end='', flush=True)
    input_str = ""
    domain_added = False
    
    while True:
        ch = read_char()
        
        # Guard clause: Block execution on shortcut signals or tab actions
        if ch == '\t' or ord(ch if ch else '\x00') < 32 and ch not in ('\r', '\n', '\x08'):
            continue
            
        if ch in ('\r', '\n'):  # Enter key pressed
            if input_str.endswith("@gmail.com"):
                print()
                return input_str
            else:
                print("\n❌ Error: Complete typing until address matches '@gmail.com'!")
                print(prompt + input_str, end='', flush=True)
                continue
                
        elif ch == '\x08' or ch == '\x7f':  # Backspace handling
            if len(input_str) > 0:
                # If removing domain, reset flag tracking status
                if input_str.endswith("@gmail.com"):
                    domain_added = False
                input_str = input_str[:-1]
                # Wipe character off the terminal interface cleanly
                sys.stdout.write('\b \b')
                sys.stdout.flush()
            continue
            
        # Standard character routing sequence
        if not domain_added:
            input_str += ch
            sys.stdout.write(ch)
            sys.stdout.flush()
            
            # Trigger dynamic autofill condition the moment user logs '@'
            if ch == '@':
                autofill = "gmail.com"
                input_str += autofill
                sys.stdout.write(autofill)
                sys.stdout.flush()
                domain_added = True

def secure_password_input(prompt, mask_text=False):
    print(prompt, end='', flush=True)
    password = ""
    
    while True:
        ch = read_char()
        
        if ch in ('\r', '\n'):  # Enter key tracking
            print()
            return password
            
        elif ch == '\x08' or ch == '\x7f':  # Backspace handling
            if len(password) > 0:
                password = password[:-1]
                sys.stdout.write('\b \b')
                sys.stdout.flush()
            continue
            
        # Block special controls or unintended shortcut keys
        if ord(ch if ch else '\x00') < 32:
            continue
            
        password += ch
        if mask_text:
            sys.stdout.write('*')  # Print secure masking indicator during login phase
        else:
            sys.stdout.write(ch)   # Show password clearly during registration phase
        sys.stdout.flush()

class User:
    name = ''
    email = ''
    password = ''
    is_authenticated = False

    def setup_account(self):
        self.name = input("Set account name: ")
        # Forces explicit typing validation rule
        self.email = secure_email_input("Set registration email: ")
        # Mask text is False -> Password prints clearly on creation screen
        self.password = secure_password_input("Set account password (Visible): ", mask_text=False)
        print("Registration completed successfully!\n")

    def authenticate_user(self):
        print(f"--- Login Portal for {self.name} ---")
        input_email = input("Enter email: ")
        # Mask text is True -> Hidden securely without any bypass options
        input_password = secure_password_input("Enter password (Hidden): ", mask_text=True)
        
        if input_email == self.email and input_password == self.password:
            self.is_authenticated = True
            print("Login successful!")
        else: 
            print("Failed: Invalid email or password")

# Execution sequence
user1 = User()
user1.setup_account()
user1.authenticate_user()
