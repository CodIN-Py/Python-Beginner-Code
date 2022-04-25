#different methods to add variables in print statements



frist_name='Python'
last_name='Beginner'
age=1




print("My name is",frist_name,last_name ,"and my age is",age)

print(f"My name is {frist_name} {last_name} and I am {age} years old")

print(f"My name is {frist_name} {last_name} and I am {age*2} years old")

print("My name is {} {} and I am {} years old".format(frist_name,last_name,age))

# %s for stings, %d for int, %f for float
print("My name is %s %s and I am %d years old" %(frist_name,last_name,age))

