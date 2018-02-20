import requests


def send_request(method, url, headers, body):
    if method == "POST":
        req = requests.post(url, headers=headers, data=body)
    elif method == "GET":
        req = requests.get(url, headers=headers)
    elif method == "PUT":
        if body is None:
            req = requests.put(url, headers=headers)
        else:
            req = requests.put(url, headers=headers, data=body)
    else:
        req = requests.delete(url, headers=headers)
    print req.text
    req.raise_for_status()
    return req
