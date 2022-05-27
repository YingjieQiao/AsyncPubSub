import redis
import time

CHANNEL = "test"
REDIS_HOST = "redis"

def main():
    r = redis.Redis(host=REDIS_HOST, decode_responses=True)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe(CHANNEL)

    while True:
        message = p.get_message()
        if message:
            print(message.get("data", ""))
        time.sleep(0.001)


if __name__ == "__main__":
    print("consumer started")
    main()
