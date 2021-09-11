# Python phone number parsing and formatting library

# Examples of use:
import os 
os.system("clear")


import phonenumbers
from phonenumbers.util import prnt  # equivalent to Py3k print()
x = phonenumbers.parse("+22243039964", None)
prnt(x) 
# Country Code: 222 National Number: 43039964
# type(x)
# <class 'phonenumbers.phonenumber.PhoneNumber'>
str(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL))
# '020 8366 1177'
#str(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
# '+44 20 8366 1177'
#str(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164))
# '+442083661177'
#y = phonenumbers.parse("020 8366 1177", "GB")
# prnt(y)
# Country Code: 44 National Number: 2083661177
# x == y
# True
# >>>
# formatter = phonenumbers.AsYouTypeFormatter("US")
#prnt(formatter.input_digit("6"))
# 6
#prnt(formatter.input_digit("5"))
# 65
#prnt(formatter.input_digit("0"))
# 650
#prnt(formatter.input_digit("2"))
# 650-2
#prnt(formatter.input_digit("5"))
# 650-25
#prnt(formatter.input_digit("3"))
# 650-253
#prnt(formatter.input_digit("2"))
# 650-2532
#prnt(formatter.input_digit("2"))
# (650) 253-22
#prnt(formatter.input_digit("2"))
# (650) 253-222
#prnt(formatter.input_digit("2"))
# (650) 253-2222
# >>>
#text = "Call me at 510-748-8230 if it's before 9:30, or on 703-4800500 after 10am."
#for match in phonenumbers.PhoneNumberMatcher(text, "US"):
#      prnt(match)
# 
# PhoneNumberMatch [11,23) 510-748-8230
# PhoneNumberMatch [51,62) 703-4800500
#for match in phonenumbers.PhoneNumberMatcher(text, "US"):
#      prnt(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))
#
# +15107488230
# +17034800500
# 
