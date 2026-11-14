#practice 5 Nov
def varMath():
#variable and math operations
    myVar = "Hello Python Test 1"

    a="Do not escape"
    b=" and do not use shortcut"

    c=2+3
    d=4-2
    e=str(d)
    integer = f,g,h = (2,3,4)

    #Print section
    print(myVar) #only text
    print(a +b)  #merge two text
    #merge text and math term or digit
    print(a +" " + str(c))  #use str() function in print function
    print(a+e) #use str() function
    print(integer)
    print(f) #leaner series variable

def Ifconditon():
#if else statements
    age = 25

    if(age >= 18):
        print("You are eligble")
    else:
        print("do not enter")

    #advanced way
    text = 5
    print("right" if text == 5 else "wrong")
    #use tenary operator
    print("kid" if age < 13 else "adult" if age >= 18 else "not adult")
    #general rules
    if age < 13:
        print("kid")
    elif age >= 18:
        print("adult")
    else:
        print("not adult")

def Loop():
#loop statements
    #while loop
    i=1
    while i<5:
        print(i+1>=5)
        i+=1

    while i<=100:
        if i%2 == 0:
            print(i)
        i+=3
    data = [2, 1,3, 4, 5,2, 9]
    #when loop count unknown
    for x in data:
        print(x)

#Function 
# def functionName(parameter): or use {}
def simpleFunction():
    print("Say hello to function")
    a,b = 4,6
    sum = a+b
    print(sum)

#output function
def Output():
    varMath()
    Ifconditon()
    Loop()
    simpleFunction()

#Output()