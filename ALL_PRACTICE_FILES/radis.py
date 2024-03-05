import redis

r = redis.Redis(host='localhost', port=6379)

r.mset({"France": "Paris", "France": "France"})

print(r.get("France"))
print(r.get("Germany"))
