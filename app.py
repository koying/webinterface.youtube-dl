import YDStreamExtractor

from cgi import parse_qs, escape

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    url = d.get('url', [''])[0]
    if not url:
        start_response('400 Bad Request')
        return [""];
      
    
    #url = "http://www.youtube.com/watch?v=DBvv2_0EV54" #a youtube ID will work as well and of course you could pass the url of another site
    vid = YDStreamExtractor.getVideoInfo(url,quality=0) #quality is 0=SD, 1=720p, 2=1080p and is a maximum
    stream_url = vid.streamURL() #This is what Kodi (XBMC) will play
    if not stream_url:
        start_response('500 Internal server error')
        return [""];

    prot_options = stream_url.find('|')
    if prot_options != -1:
        stream_url = stream_url[:prot_options]

    start_response('302 Temporary Redirect', [('Location',stream_url)])
    return [""]    

#    response_headers = [
#        ('Content-Type', 'text/html'),
#        ('Content-Length', str(len(stream_url)))
#    ]

#    start_response('200 OK', response_headers)
#    return [stream_url]
    
    
