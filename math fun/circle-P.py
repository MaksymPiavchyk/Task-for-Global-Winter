from flask import escape
from math import pi
def circle_P(request):
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
        P = 2 * pi * r
    elif request_json and 'r' in request_json:
        r = (request_json['r'])
        P = 2 * pi * r
    else:
        P = 'Error code'
    return escape(P)
