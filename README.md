lti4web2py
==========

An IMS Learning Tools Interoperability (LTI) 1.x Provider Application for Web2Py

The basic idea is that you can add this application to your web2py instance and 
use LTI to create accounts and log users in.

This code requires sessions to be stored in a database so that we can set 
the session of another application and the redirect to that application. 
It also requires that we share the aut of that application.  If this tool
will be used to frontend more than one application - all applications need 
to share one set of auth tables.

This is a very early version of the code.  Comments welcome.

Install Notes
=============

Check out the code into the applications folder in your web2py from github.

You need to make a folder called "lti2web2py/databases" - I cannot tell if
I am supposed to make this or not.

You will have to go into the application that you will be using LTI to 
front-end and do a few things.  I will use applications/welcome as my example.

You will need the same DAL configuration in lti4web2py/models/db.py as in
welcome/models/db.py - lookg for the creation of the DAL and copy the line.

Look for the auth.define_tables() call.  Make sure the 'username=True' is
one of the parameters.  LTI uses username-style login instead of email style
login.

auth.define_tables(username=True, signature=False)

You need to add a session.connect() somewhere in welcome/models/db.py to 
override the default of storing in the file system.  We need these in a database
to allow them to be shared across applications (i.e. set in LTI and read in 
the destination application).

I added the line right after the DAL creation in welcome/models/db.py

db = DAL('mysql://web2py:web2pypassword@localhost/web2py',pool_size=1,check_reserved=['all'])
session.connect(request, response, masterapp='welcome', db=db)

Edit lti4web2py/models/db.py and change the DAL to match the DAL
in welcome/models/db.py

The session.connect will happen later.

Navigate directly to the URL http://127.0.0.1:8000/lti4web2py/default/ 
(substitute your host and port)

This will complain with "user_id is required for this tool to function" -
this is OK.   What we really accompished is the creation of the lti_keys
table in the database.

    mysql> describe lti_keys;
    +-------------+--------------+------+-----+---------+----------------+
    | Field       | Type         | Null | Key | Default | Extra          |
    +-------------+--------------+------+-----+---------+----------------+
    | id          | int(11)      | NO   | PRI | NULL    | auto_increment |
    | consumer    | varchar(512) | YES  |     | NULL    |                |
    | secret      | varchar(512) | YES  |     | NULL    |                |
    | application | varchar(512) | YES  |     | NULL    |                |
    +-------------+--------------+------+-----+---------+----------------+
    4 rows in set (0.01 sec)

Next insert a consumer, secret, and application similar to the following:

    mysql> select * from lti_keys;
    +----+----------+--------+-------------+
    | id | consumer | secret | application |
    +----+----------+--------+-------------+
    |  1 | 12345    | secret | welcome     |
    +----+----------+--------+-------------+
    1 row in set (0.00 sec)
 
Make sure the application matches the application we are front-ending.  It is 
possible to front-end more than one application at the same time but we will 
just stick with one for now.

Testing
=======

The next step is to do a test-launch to your application.  Go to 

https://online.dr-chuck.com/sakai-api-test/lms.php

Fill in the URL, key, and secret.   The URL should be similar to:

http://127.0.0.1:8000/lti4web2py/default/
(substitute your host and port)

Press "Launch"  - If all goes well the next thing you will see is a 
new window popped up in the Web2Py Welcome application (or your 
application) that says "Welcome Siân".

If you see this, all is working.  If not, the standard output 
of your web2py will be littered with print statements and the browser 
window should have some explanation as to what went wrong.

Let me know how it goes.

/Chuck
Tue Jan  7 02:56:18 EST 2014


