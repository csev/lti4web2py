# import oauth
# import oauth_store

oauth = local_import('oauth',reload=True)
oauth_store = local_import('oauth_store',reload=True)

print "In imslti.py"
# print dict(request.vars)

oauth_server = oauth.OAuthServer(oauth_store.LTI_OAuthDataStore(db))
oauth_server.add_signature_method(oauth.OAuthSignatureMethod_PLAINTEXT())
oauth_server.add_signature_method(oauth.OAuthSignatureMethod_HMAC_SHA1())

# Reconstruct the incoming URL
if request.is_https : 
    full_uri = 'https://' 
else :
    full_uri = 'http://'
full_uri = full_uri + request.env.http_host + request.env.request_uri

oauth_request = oauth.OAuthRequest.from_request('POST', full_uri, None, dict(request.vars))

consumer = None
token = None
params = None
oauth_error = None
try:
    print "Incoming request from:", full_uri
    consumer, token, params = oauth_server.verify_request(oauth_request)
    print "Verified."
except oauth.OAuthError, err:
    oauth_error = "OAuth Security Validation failed:"+err.message
    print oauth_error
    consumer = None
except:
    print "Unexpected error"
    oauth_error = "Unexpected Error"
    consumer = None

# Time to create / update / login the user
if consumer is not None:
    print params
    user_id = params['user_id']
    last_name = params['lis_person_name_family']
    first_name = params['lis_person_name_given']
    email = params['lis_person_contact_email_primary']

    userinfo = dict()
    userinfo['first_name'] = first_name;
    userinfo['last_name'] = last_name;
    userinfo['email'] = email;
    userinfo['username'] = consumer.key + ":" + user_id;
    print db.auth_user
    print db.auth_user.password
    print db.auth_user.password.validate('1C5CHFA_enUS503US503')
    pw = db.auth_user.password.validate('1C5CHFA_enUS503US503')[0];
    print pw 
    userinfo['password'] = pw
    print userinfo
    user = auth.get_or_create_user(userinfo, update_fields=['email', 'first_name', 'last_name', 'password'])
    print user, type(user)
    print "Logging in..."
    retval = auth.login_user(user)
    print "Logged in...", retval, type(retval)
    # context_id = params['context_id']


