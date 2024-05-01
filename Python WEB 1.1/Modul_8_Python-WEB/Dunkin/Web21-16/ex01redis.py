import redis


r = redis.Redis(host="localhost", port=6379, password=None)

r.set(10, "Привіт")

value = r.get(10).decode()
print(value)# bar

# r.set("foo", "Hello")
