
def index():
    print "In my index"
    if consumer is None:
        return "BAD MOJO"
    print params
    user_id = params['user_id']
    context_id = params['context_id']
    print user_id, context_id
    return "WOO HOO!!!"

def user():
    print "ZIPPY"
    return "YO"

