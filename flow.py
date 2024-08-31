from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    url = flow.request.url
    if 'https://speed.cloudflare.com/__down' in url:
        bytes_value = flow.request.query.get('bytes')
        if bytes_value:
            flow.response = http.Response.make(200, b'0' * int(bytes_value), {'Content-Type': 'application/octet-stream'})
    elif 'https://speed.cloudflare.com/__up' in url:
        flow.response = http.Response.make(200, b'', {'Content-Type': 'application/octet-stream'})
        