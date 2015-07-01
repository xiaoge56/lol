import urllib2
req = 'http://www.jb51.net/213123'
try:  
    response = urllib2.urlopen(req)
    
except urllib2.HTTPError, e:  
    print 'The server couldn\'t fulfill the request.'  
    print 'Error code: ', e.code  
except urllib2.URLError, e:  
    print 'We failed to reach a server.'  
    print 'Reason: ', e.reason  
else:  
    print 'No exception was raised.'  
    html=response.read()
    print html
