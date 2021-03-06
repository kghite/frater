from dataclasses import dataclass, field

from pymongo import MongoClient

from .stream import InputStream, OutputStream
from ..config import Config
from ..io import json_to_frater, frater_to_json


@dataclass
class MongoStreamConfig(Config):
    name: str = 'mongo_stream_config'
    host: str = 'localhost'
    port: int = 27017
    db: str = 'db'
    collection: str = 'collection'
    filter: dict = field(default_factory=dict)


class MongoInputStream(InputStream):
    def __init__(self, config: MongoStreamConfig = None, data_type=None):
        super(MongoInputStream, self).__init__(data_type)
        self.config = config if config is not None else MongoStreamConfig()
        self.client = MongoClient(self.config.host, self.config.port)

    @property
    def db(self):
        return self.client[self.config.db]

    @property
    def collection(self):
        return self.db[self.config.collection]

    def __iter__(self):
        for item in self.collection.find(filter=self.config.filter):
            yield json_to_frater(item)


class MongoOutputStream(OutputStream):
    def __init__(self, config: MongoStreamConfig = None, data_type=None):
        super(MongoOutputStream, self).__init__(data_type)
        self.config = config if config is not None else MongoStreamConfig()
        self.client = MongoClient(self.config.host, self.config.port)

    @property
    def db(self):
        return self.client[self.config.db]

    @property
    def collection(self):
        return self.db[self.config.collection]

    def send(self, data):
        self.collection.insert_one(frater_to_json(data))
