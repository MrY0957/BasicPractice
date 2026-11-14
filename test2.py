#November 6
def statements():
    #single line
    print("Python is fun!")
    #use only one semicolon and single ' ' quatation
    print('not that');
    #multi in one line
    print("do  not do"); print("bye")
    #adding space by end=" "
    print('hello py', end=" "); print('thanks to do')
#statements()

def numberPrint():
    print(3); print(0.59); print(100)
    print(3+7); print(3*8)
    #text+num or math
    print("null", 0, " used")
    #Type Conversion casting
    x=str(3)
    print(type(x))
#numberPrint()
#Repeat loop Actions
def Loopf():
    for i in range(5):
        print(i)
#Loopf()
#Assigning Value to multi var
def check_unpacking_and_loops():
    # 1. Multi-variable assignment
    x, y, z = 'orange', 'banana', 'mango'
    a="hello, world"
    b="thanks again"
    c="PYTHON"
    d="core3:"
    e="123059"
    f=12
    g="my digit is {}"
    
    print("length: ",len(b)) #length of variables

    print("string methods")
    print(x.upper()) #capital letter character
    print(y.lower()) #small letter character
    print(a.swapcase()) #low to up or up to lower case
    print(a.title()) #first word capital
    print(b.capitalize()) #first letter capital
    
    print("space releated methods")
    print(z.strip()) #extra space remove
    print(a.lstrip()) 
    print(a.rstrip())
    
    print("Replace & split methods")
    print(a.split(",")) #list in string
    print(x.replace("o","T")) #replace character
    print(y.replace("banana", "sugar")) #replace word
    
    print("search methods")
    print(b.find("again")) #Find position return in word 
    print(b.count("a")) #count word
    print(b.index("again")) #find()
    
    print("checking methods")
    print(c.isupper()) #check case true or false
    print(d.isalpha()) #check just letter or not?
    print(e.isnumeric()) #check just numeric value
    print(a.startswith("hello")) #check word in first line
    print(b.endswith("again")) #check word in end line
    print(e.isdigit()) #check digit
    print(x.islower()) #check lower 
    
    print("Formatting Methods")
    print(z.center(20))
    print(e.zfill(5))
    print(g.format(f))
    
    """ # 2. Perfect Unpacking (Variables match element count)
    color_list = ['red', 'black', 'yellow', 'white']
    x, y, z, w = color_list 
    print(x+y+z)
    
    # 3. Independent Sequential Loops
    numbers = [1, 2, 3, 4, 5]
    for n in numbers:
        print(f"Outer Loop 1 (Item): {n}")
     
    for step in range(3):
        print(f"Inner Loop 2 (Step): {step}") """
check_unpacking_and_loops()

def print_specific_range():
    items = ['red', 'black', 'yellow', 'white', 'green', 'blue']
    
    # Target range using loop: index 2 up to 4 ('yellow', 'white', 'green')
    print("\n--- Method 1: Index Control via range() ---")
    for i in range(2, 5):
        print(f"Index {i}: {items[i]}")
        
    print("\n--- Method 2: Iterating Over Sliced List ---")
    for item in items[2:5]:
        print(f"Value: {item}")
#print_specific_range()


