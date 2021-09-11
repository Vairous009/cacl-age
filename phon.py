import os
os.system("clear")

print("\033[0;32 ===> desing by SF7.RIM <===\n")
bonne ='''
   _____ ______ ______ _____  _____ __  __ 
  / ____|  ____|____  |  __ \|_   _|  \/  |
 | (___ | |__      / /| |__) | | | | \  / |
  \___ \|  __|    / / |  _  /  | | | |\/| |
  ____) | |      / /  | | \ \ _| |_| |  | |
 |_____/|_|     /_(_) |_|  \_\_____|_|  |_|
  
'''
print(bonne)

import phonenumbers
from test import number
from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number, 'CH')
print(geocoder.description_for_number(ch_nmber, 'en'))

#  m3rvt chebeke 
from phonenumbers import carrier  
service_nmbre = phonenumbers.parse(number, 'RO')
print(carrier.name_for_number(service_nmbre, 'en'))