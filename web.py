from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<title>Top Software Industries</title>
<body>
<table border="2" cellspacing="10" cellpadding="6">
<caption>Top 5 Revenue Generating Software Companies </caption>
<tr>
DAR
<th>s.no</th>
Nouve
<th>companies</th>
<th>revenue</th>
New
Voy </tr>
<tr> I
D
<th>1</th>
NAUKA
<th>Microsoft</th>
PARKO
<th>65 billion</th>
</tr>
<tr>
CALKA
NA <th>2</th>
<th>oracle</th>
Nemze
<th>29.6 billion</th>
Vanes
</tr>
Vers
<tr>
NOK
<th>3</th>
Saun
<th>IBM</th>
New
<<thth> >29.1 billion</th>
</tr>
<tr>
<th>4</th>
<th>SAP</th>
<th>6.4 billion</th>
hos
</tr>
DAN
<tr>
AKSE th>5</th>
<
<th>symentec</th>
<th>5.6 billion</th>
</body>
/html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()