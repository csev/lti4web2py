import oauth

class LTI_OAuthDataStore(oauth.OAuthDataStore):

    db = None

    def __init__(self, db):
        self.db = db
        pass

    def lookup_consumer(self, key):
        myrecord = self.db(self.db.lti_keys.consumer==key).select().first()
        # print myrecord, type(myrecord)
        if myrecord is None : return None
        return oauth.OAuthConsumer(key, myrecord['secret'])

    # We don't do request_tokens
    def lookup_token(self, token_type, token):
        return oauth.OAuthToken(None, None)

    # Trust all nonces
    def lookup_nonce(self, oauth_consumer, oauth_token, nonce):
        return None

    # We don't do request_tokens
    def fetch_request_token(self, oauth_consumer):
        return None

    # We don't do request_tokens
    def fetch_access_token(self, oauth_consumer, oauth_token):
        return None

    # We don't do request_tokens
    def authorize_request_token(self, oauth_token, user):
        return None
