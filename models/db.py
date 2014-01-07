from gluon.tools import Auth

# Make sure to match this with the models/db.py in welcome we we share auth tables
db = DAL('mysql://web2py:web2pypassword@localhost/web2py',pool_size=1,check_reserved=['all'])

auth = Auth(db)

# Note - welcome/models/db.py should have username=True to insure username field exists
auth.define_tables(username=True, migrate=False)

# Define our tables
db.define_table('lti_keys', Field('consumer'), Field('secret'), Field('application'))

# print "LTI db.py", type(db), type(auth)
