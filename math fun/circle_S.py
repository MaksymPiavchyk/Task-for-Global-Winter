from flask import escape
from math import pi
def circle_S(request):
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
    
    if request_args and 'r' in request_args:
        r = int(request_args['r'])
        S = pi * r ** 2
    elif request_json and 'r' in request_json:
        r = request_json['r']
        S = pi * r ** 2
    else:
        S = 'Error code'
    return escape(S)
