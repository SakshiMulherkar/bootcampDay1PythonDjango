import cgi
import cgitb
from builtins import KeyError

from django.shortcuts import redirect

try:
    form = cgi.FieldStorage()
    fn = form.getvalue('f1.html')
    ln = form.getvalue('f1.html')
    e = form.getvalue('f1.html')
    t = form.getvalue('f1.html')
    co = form.getvalue('f1.html')
    c = form.getvalue('f1.html')
    print("Name",fn,ln)
    print("Email", e)
    print("telephone", t)
    print("country", co)
    print("city", c)
except KeyError:
    print("error")
else:
    data_to_be_displayed = fn,ln,e,t,co,c# data to be used in connect.php; it's an array of ids

    import httplib, json, urllib2
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    conn = httplib.HTTPConnection('192.168.56.101:80')

    data_to_be_displayed = json.dumps(data_to_be_displayed, ensure_ascii = 'False')
    conn.request("POST", "f1.html", data_to_be_displayed, headers)
    response = conn.getresponse()
    text = response.read()

    conn.close()


    if response.status == 200:
        redirect('f2.html')
