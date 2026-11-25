import platform

def app(environ, start_response):
    body = platform.python_version().encode()
    start_response("200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(body)))])
    return [body]
