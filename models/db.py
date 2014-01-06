
from gluon.tools import Auth

# Make sure to match this with the models/db.py in welcome we we share auth tables
# db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
db = DAL('mysql://web2py:web2pypassword@localhost/web2py',pool_size=1,check_reserved=['all'])

auth = Auth(db)
auth.define_tables(migrate=False)

# Define our tables
db.define_table('lti_keys', Field('consumer'), Field('secret'), Field('application'))

# print "in db.py", type(db), type(auth)

# print "insert", db.lti_keys.insert(consumer="12345", secret="secret")
# db.commit()
