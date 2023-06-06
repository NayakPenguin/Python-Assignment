def validate_phone_number(phone_number):
    if(len(phone_number) == 10) :
        return True
    else :
        return False

phone_number = input("Enter a phone number : ")

if validate_phone_number(phone_number):
    print("Valid phone number")
else:
    print("Invalid phone number")