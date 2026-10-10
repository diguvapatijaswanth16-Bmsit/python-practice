student_marks={"jaswanth":93,
       "anu":89,
       "reddy":73,
       "jashu":66,
       "dfgfha":32,
       "werfj":56
}
student_grade={}
for student in student_marks:
    marks=student_marks[student]
    if marks>90:
        student_grade[student]="A+"
    elif marks>80:
        student_grade[student]="A"
print(student_grade)

countries={"india":{"andhra":10,
                    "telengana":23,
                    "bangalore":34
            },
            "us":{"iran":10,
                  "german":38
            }
}
for country in countries:
    print(countries[country])
import os
name=input("please enter your name")
bit_value=int(input("please enter the bit valus that you want to enter"))
yes_no=input("is any body there to bit(yes/no)")
store={}
store[name]=bit_value
while yes_no=="no":
    name=input("please enter your name")
    bit_value=int(input("please enter the bit valus that you want to enter"))
    yes_no=input("is any body there to bit(yes/no)")
    store[name]=bit_value
largest_number=0
for names in store:

    if i>largest_number:
        largest_number=i



        
    

def add(a,b):
    c=a+b
    return

print(add(2,3))

name="jaSWANth reddy"
print(name.title())
import statistics
def mean_mode_median(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
a,b,c=mean_mode_median([1,2,3,3,4,23,1])
print(a)
print(b)
print(c)
import statistics
def sta(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
a,b,c=sta([1,24,3,2,3,4,5])
print(a)
print(b)
print(c)
a=float(input("please enter the first number"))
b=float(input("please enter the second number"))
def num(a,b):
    if a==0 and b==0:
        
        return "this number does not exists"
        
    else:
        return a+b
answer=num(a=float(input("please enter the first number\n")),b=float(input("please enter the second number\n")))
print(answer)

def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def year_month(year,month):
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month==2:
        return 29
    else:
        return days[month-1]
number=year_month(int(input("piease enter the year\n")),int(input("please enter the month\n")))
print(number)





def function(a,b):
    c=a+b
    print(c)
sum=function(4,5)
print(sum)


a=10
def value():
    global a
    a+=1
    def inside():
        
        
        print(a)
    inside()

    
value()

print(a)


n=int(input().strip())
# print("not weird"if (n%2==0 and n>20) or (n%2==0 and 2<=n<=5)else "weird")


l=[1,3,4,32,4,32,54]
l.sort()
print(l)