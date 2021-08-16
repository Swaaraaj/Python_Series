import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

number1 = input("Enter Phone_No :")
ph_no = phonenumbers.parse(number1)

print(geocoder.description_for_number(ph_no,"en"))
print(carrier.name_for_number(ph_no,"en"))


# While input give in format like:
# +91 phonenumber