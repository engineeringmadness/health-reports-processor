from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

class PostgresConnection:

    def __init__(self):
        self.user = os.environ['PG_USER']
        self.password = os.environ['PG_PASSWORD']
        self.host = os.environ['PG_HOST']
        self.port = os.environ['PG_PORT']
        self.database = os.environ['PG_DATABASE']
        # Setup connection pooling to handle multiple workflows using common connection
        self.engine = create_engine(
            url=f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}',
            pool_size=10,
            max_overflow=2
        )

    def get_session(self):
        return sessionmaker(bind=self.engine)()

db = PostgresConnection()