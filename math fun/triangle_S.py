from flask import escape
def triengle_S(request):
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
    
    if request.args and 'b' and 'h' in request.args:
        
        b = request_args['b']
        h = request_args['h']
        S = (b * h)/2
    elif request_json and 'b' and 'h' in request_json:        
	        
        b = request_json['b']
        h = request_json['h']
        S = (b * h)/2
    else:
        S = 'Error code'
    return escape(S)
