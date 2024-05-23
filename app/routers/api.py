from typing import Annotated

from fast_depends import Depends
from fastapi import APIRouter
from faststream.kafka.fastapi import KafkaRouter, KafkaBroker

from app.broker import broker, router as kafka_router

api_router = APIRouter(prefix="/api", tags=["api"])


@api_router.get("/hello/{name}")
async def hello(name: str, kafka: Annotated[KafkaBroker, Depends(broker)]):
    await kafka.publish(name, "hellos_topic")
    return f"Hello, {name}!"
