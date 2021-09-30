import datetime
import random

username = input("Enter Your name : ")
print ("Hello " + username + "!")

a=random.random()
print("Your one time unique ID is gernerated : ", a)

a=datetime.datetime.now()
print("Date & timing of registration :",a)
