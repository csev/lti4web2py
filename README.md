lti4web2py
==========

An IMS Learning Tools Interoperability (LTI) 1.x Provider Application for Web2Py

Install Notes
=============

In the file welcome/models/db.py

auth.define_tables(username=True, signature=False)

session.connect(request, response, masterapp='welcome', db=db)



