from fastapi import APIRouter

from app.broker import User, avro_producer

api_router = APIRouter(prefix="/api", tags=["api"])


@api_router.get("/hello/{name}")
async def hello(name: str):
    u = User(name=name)
    avro_producer.produce(topic="greetings", value=u.dict())
    avro_producer.flush()
    return f"Hello, {name}!"
