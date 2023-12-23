#print("Rohan islam")
#print('0-----')
#print("  ||||")
#print('*'*10)


#Variables
#price=10
#rating=4.6
#name="Rohan"
#is_published=False,True
#print(price,rating,name,is_published)

"We check in a patient named Daud islam.He's 20 years old and is a new patient."
#name="Daud Islam"
#Age="20"
#is_new=True

#Getting input
#name= input('what is your name?= ')
#print('Hi ' + name)

"Ask two questions: person's name and favourite color. then, print a message like'Mosh likes blue'"
#name=input("What is your name= ")
#favourite_color=input("What is your favorite color= ")
#print(name, "Likes "+favourite_color)
"------------------------------------------"
#Type Conversion
#birth_year=input('Birth year: ')
#age=2023-int(birth_year)
#print("YOU ARE",age , "years old.")

"ASk a user their weight(in pounds),convert it to kilograms and print on the tirmenal."
#weight_lbs=input('Weight (lbs): ')
#weight_kg=int(weight_lbs) *(0.45)
#print(weight_kg)

#weight_kg=input('Wight(kg): ')
#weight_lbs=float(weight_kg)*0.45
#print("You are ",weight_lbs ,"pound")
"-------------------------------------------"
#String
#course="python's course  for Beginners"
#cour='python for "Beginners"'
coru='''
Hi Rohan,
How are you .
i,am fine .
Thanks for your massege
'''
#print(coru)
#course='python for Beginners.'
#print(course[0:])
"----------------------------------------"
#Formatted Strings
#first='jhon'
#last='smith'
#rint(f"{first} [{last}] is a coder")
"------------------------------------------"
#string Methods
course='python for Beginners'
#print(len(course))
#print(course.upper())
#print(course.lower())
#print(course.find("f"))
#print(course.replace('Beginners','Absolute Beginners you have practice python more and more'))
#print(course.replace('for','and Django and Mshaing larning, artefheail intelegent for '))
#print("python"in course)
"------------------------------------------"
#Arithnetic Operations
#print( 5//3)
#x=10
#x=x+3
#x+=4
#x-=2
#x*=2
#print(x)
"------------------------------------------"
#Operator Precedence
x=10+3*2
#print(x)
x=(2+3)*10-3
#print(x)
"--------------------------------------------"
#Math Functions
import math    #python math module Google.
#print(math.ceil(2.9))
#rint(math.floor(2.9))
#x=2.9
#rint(round(x))
#rint(abs(-x))
"-------------------------------------------"
#if Statement
is_hot=True
is_could=False
#if is_hot :
    #print("It's a hot day")
    #print("Drink plenty water")
#elif is_could:
    #print("It's a cold day")
    #print("Wear warm clothes")
#else:
    #print("It's a Lovly day.")
#print("Enjoy your day.")
"---------------------------------------------"
#QUA: price of a house is $1M. 
#     if buyer has good crredit,
        #They need to put down 10%
#     otherwise
#        they need to put down 20%
#     print the down payment
    
#price=1000000
#has_good_credit=True

#if has_good_credit:
 #   down_payment=0.1*price
#else:
 #   down_payment=0.2*price
#print(f"Down payment: ${down_payment}")

"----------------------------------------"
#Logical Operators
#has_hight_income=True
#as_good_credit=True
#if has_hight_income and has_good_credit:      #and
 #   print("Elegable for Lon")

#has_hight_income=True
#has_good_credit=False
#if has_hight_income or has_good_credit:       #Or
 #   print("Elegable for Lon")

#has_good_credit=True
#has_criminal_record=True
#if has_good_credit and not has_criminal_record:     # and not
 #   print("Eligable for loan")
#else:
#    print("dont Eligable for loan")

#has_high_income=True    #and or and not (Every think)
#has_good_credit=True
#if has_high_income and has_good_credit:
 #   print("Eligeble for lone")
#elif has_high_income or has_good_credit:
#    print("Think and Eligable for lone")
#else:
#    print("Don't Elegable for lone")
"---------------------------------------------------------------"

#comparison Operator
#tempre=32
#if tempre >30:
#   print("It's a hot day")
#else:
#    print("It's a Good day")    
'-----------------------------------------------------------'

#name='Ro'
#if len(name)<3:
#    print("Name Must be 5 crecter")
#elif len(name)>50:
#    print("Name miximum 50 crecter.")
#else:
#    print("names looks Good.")
'----------------------------------------------------------------'
#Guess Game
#secret_Number=8
#uess_count=0
#uess_limit=3
#while guess_count<guess_limit:
#    guess=int(input("Guess: "))
#    guess_count+=1
#    if guess ==secret_Number:
#       print("you win!")
#       break
#lse:
#   print("Sorry you are faild.")
'-----------------------------------------------------------------'

#Car Game.
#commend=""
#started=False
#while True:
#    commend=input("> ").lower()
#    if commend=="start":
#        if started:
#            print("car Allredy started")
#        else:
#            started= True
#           print("Car started.......")
#    elif commend=="stop":
#        if not started:
#            print("car allredy stoped.")
#        else:
#           started=False
#           print("Car stoped.........")
#   elif commend=="help":
#        print("""
#Start - to start the car
#stop - to stop the car
#quit - to quit the car
#        """)
#    elif commend =="quit":
#        break
#    else:
#        print("Sorry I don't understand it.")
"-----------------------------------------------------------"

#For Loops
for item in [1,2,3,4,5]:
    print(item)
for i in range(10):
    print(i)
