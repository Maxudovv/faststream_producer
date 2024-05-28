from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
from pydantic import BaseModel


class User(BaseModel):
    name: str


schema_registry_url = "http://schema-registry:8081"
kafka_broker = "kafka:9092"
topic = "greetings"

value_schema_str = """
{
  "namespace": "greetings",
  "type": "record",
  "name": "Greeting",
  "fields": [
    {"name": "name", "type": "string"}
  ]
}
"""
value_schema = avro.loads(value_schema_str)

avro_producer_config = {
    "bootstrap.servers": kafka_broker,
    "schema.registry.url": schema_registry_url,
}
avro_producer = AvroProducer(avro_producer_config, default_value_schema=value_schema)
