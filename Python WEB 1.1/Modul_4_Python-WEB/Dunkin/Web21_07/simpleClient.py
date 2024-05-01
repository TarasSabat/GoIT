from http import client


h1 = client.HTTPConnection('localhost', 8001)
print("Client start")
h1.request("POST", "/")

res = h1.getresponse()
print(res.status, res.reason)

data = res.read()
print(data)