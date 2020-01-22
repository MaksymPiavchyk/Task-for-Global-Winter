import math
def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json(silent=True)
    def degreesToRadians(degrees):
        return(degrees * math.pi)/180
    def distanceInKmBetweenEarthCooedinates(lat1, lon1, lat2, lon2):
        earthRadiusKm = 6371
        dLat = degreesToRadians(lat2-lat1)
        dLon = degreesToRadians(lon2-lon1)
        lat1 = degreesToRadians(lat1)
        lat2 = degreesToRadians(lat2)
        a = (math.sin(dLat/2)* math.sin(dLat/2)) + (math.sin(dLon/2) * math.sin(dLon/2) * math.sin(lat1) * math.sin(lat2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return earthRadiusKm * c
    return f'{distanceInKmBetweenEarthCooedinates(request_json["lat1"],request_json["lon1"],request_json["lat2"],request_json["lon2"],)}'
