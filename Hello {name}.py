def hello(request):
    request_json = request.get_json(silent=True)
    if request.args and 'name' in request.args:
        return f"Hello, {request.args.get('name')}"
    elif request_json and 'name' in request_json:
        return f"Hello, {request_json['name']}"
    else:
        return f"Hello, World!"
