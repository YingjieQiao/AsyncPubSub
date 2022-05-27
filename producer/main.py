from fastapi import FastAPI
import redis


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/train/{message}")
async def train(message: str):
    publish(message or "test message")

    return {"message": message}

CHANNEL = "test"
REDIS_HOST = "redis"


def publish(message):
    r = redis.Redis(host=REDIS_HOST)
    r.publish(CHANNEL, message)

