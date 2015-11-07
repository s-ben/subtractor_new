import os
from django.conf import settings # adding to try and fix error...

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "subtractor.settings")  #adding to try and fix worker error...

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

print "redis_rl"
print redis_url

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()