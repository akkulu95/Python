password = input("Enter the Password : ")
result = {} #{} indicates dictionary
#check if the password has more than 8 length

if len(password) >=0:
    result["Length"]=True
else:
    result["Length"]=False
#check whether the password has digits
digit = False
for i in password:
    if i.isdigit():
        digit = True
result["Digit"]=digit
#check whether the password has uppercase letter
uppercase = False
for i in password:
    if i.isupper():
        uppercase=True
result["uppercase"]=uppercase
#print(all(result)) #all function returns false even if one of the output is false it returns true only if all is true
if all(result.values()):
    print("Strong Password ")
else:
    print("Weak password ")


#print(result)
