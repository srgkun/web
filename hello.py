def application(environ, start_response):
    request=[]
    for i in environ['QUERY_STRING'].split('&'):
        request.append((i+'\n').encode())
        #print(i)
    #print(request)
    start_response("200 OK", [("Content-Type", "text/plain")])
    return request