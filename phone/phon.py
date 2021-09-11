print("===> desing by SF7.RIM <===\n")

import phonenumbers
from test import number
from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number, 'CH')
print(geocoder.description_for_number(ch_nmber, 'en'))

#  m3rvt chebeke 
from phonenumbers import carrier  
service_nmbre = phonenumbers.parse(number, 'RO')
print(carrier.name_for_number(service_nmbre, 'en'))