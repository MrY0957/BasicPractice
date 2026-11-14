#Constructor & Initializer
'''class TestClass:
    def __init__(self):
        print("I am a constructor")
    def function1(self):
        print("I am a function")
    def function2(self):
        print("I am another function")
#Object create and run
ob = TestClass()
ob.function2()   #initial method all time call if any method call at that time

#Tuples
list = [2,3, 212, 33, 21, 4, 4, 56]
tuple = (8,9,7,6,3,2,1,11)
#modify list
list[2]= 12
#no modifying and get Typerror: tuple[3] = 600
print("Lists can modify easily & easy to use")
print(list[2]) #before 212, after modifying 12
print(list) 
print(list[-1]) #output the last element & it works by - (minus sign)
print("Tuples can not modify the element and rare to use")
print(tuple[3]) #output: 6
print(tuple)
print(tuple[-1]) #last element of tuple print
'''

#In python, elements are stored in mix:
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,"python"]
nestedList1 = [[1,2,3],4,5,"hello"]
nestedList2 = [1,[2,"bye"], [3,4,["good", 5],6],7]

print(nestedList1[0]) #output 1st elem. [1,2,3]
print(nestedList1[0][0]) #1st [] calls index & 2nd [] calls 2nd nested list index
print(list2[-1])
print(nestedList2[2][2][0]) #print multi list

#list Operation(delete, insert, count, etc...)
list1.append(22) 
print("at last just new data add 22: ", list1)
'''insert as new data in specific index
    Syntax    ListName.insert(indexNo, NewData)
    here index number never work as -indexNo
'''
list2.insert(1, "world")
 #
list1.extend([22,44,66])
print("combine 2 lists with extend",list1)
list2 = list2 + [1,2,3] #[1,2,3] is new list but no name
print("combine 2 lists with another way",list2)

list1.remove(44) #remove only 1st element
print(list1)
list1.remove(22) 

print(list1)
print(list2[1])
print(list2)