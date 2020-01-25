# -*- coding: utf-8 -*-

""" 
Wifi password view @codehub 
"""
from subprocess import check_output

print("""
#     #                                                           
#  #  # # ###### #           #    # # ###### #    # ###### #####  
#  #  # # #      #           #    # # #      #    # #      #    # 
#  #  # # #####  #   #####   #    # # #####  #    # #####  #    # 
#  #  # # #      #           #    # # #      # ## # #      #####  
#  #  # # #      #            #  #  # #      ##  ## #      #   #  
 ## ##  # #      #             ##   # ###### #    # ###### #    # 
""")

stored = check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in stored if "All User Profile" in i]

for i in profiles:
    results = check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print(f"Wi-fi: {i} >> Password: {results[0]}")
    except IndexError:
        print(f"Wi-fi: {i} >> Empty password")

