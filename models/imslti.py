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


