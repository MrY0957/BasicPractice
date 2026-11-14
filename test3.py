#7 Nov 2026
#parameter use as text, number and everything
def sum(a,b): #function use parameter
    sum=a+b
    print(sum)
sum(2,4)

def sub(a,b=10): #with default val
    print(a, "-", b)
sub(5) #for default val
sub(4,2) #not access default val
a=5
def digit():
    global a #bad practice
    a+=1
    print(a)
    
digit()
c = 4
def digit():
    locals = c  # 'locals' এ ৪ জমা হলো
    locals = locals + 2  # 'locals' এর মান ৬ হলো
    print(c)  # গ্লোবাল c প্রিন্ট হচ্ছে। Output: 4
    print(locals) #output: 6

digit()

def digit_fixed(input_val):
    # ফাংশনের ভেতর লোকাল হিসাব করা
    updated_val = input_val + 2
    return updated_val  # নতুন মানটি ফাংশনের বাইরে ফেরত পাঠানো

# ফাংশন কল করে রিটার্ন করা মান দিয়ে গ্লোবাল 'c' কে আপডেট করা
c = digit_fixed(c)
print(c)  # এবার c এর মান সত্যি পরিবর্তিত হয়েছে। Output: 6
