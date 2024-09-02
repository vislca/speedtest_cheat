from mitmproxy import http


down_bytes = [0, 100000, 1000000, 10000000, 25000000, 100000000]
responces = {i : http.Response.make(200, b'0' * i, {'Content-Type': 'application/octet-stream'}) for i in down_bytes}
print('waiting for request...')
def request(flow: http.HTTPFlow) -> None:
    url = flow.request.url
    if 'https://speed.cloudflare.com/__down' in url:
        bytes_value = int(flow.request.query.get('bytes'))
        if bytes_value in down_bytes:
            flow.response = responces[bytes_value]
        else:
            print('bytes_value:', bytes_value)
            flow.response = http.Response.make(200, b'0' * bytes_value, {'Content-Type': 'application/octet-stream'})
    elif 'https://speed.cloudflare.com/__up' in url:
        flow.response = responces[0]
    elif 'cloudflare.com/__log' in url:
        flow.response = http.Response.make(200, b'ok', {'Content-Type': 'text/plain;charset=UTF-8'})