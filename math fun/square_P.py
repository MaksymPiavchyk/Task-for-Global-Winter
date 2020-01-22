from flask import escape
def square_P(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    request_json = request.get_json()
    request_args = request.args
    
    if request_args and 'a' in request_args:
        a = int(request_args['a'])
        P = 4 * a
    elif request_json and 'a' in request_json:
        a = request_json['a']
        P = 4 * a
    else:
        P = 'Error code'
    return escape(P)
