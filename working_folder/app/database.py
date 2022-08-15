import os
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Numeric, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

api_config = {
    'host': os.getenv("POSTGRES_HOST", "localhost"),
    'port': os.getenv("POSTGRES_PORT", "5432"),
    'dbname': os.getenv("POSTGRES_DB", "weather_data"),
    'user': os.getenv("POSTGRES_USER", "postgres"),
    'password': os.getenv("POSTGRES_PASSWORD", "postgres")
}

conn_str = f'postgresql+psycopg2://{api_config["user"]}:{api_config["password"]}@{api_config["host"]}:{api_config["port"]}/{api_config["dbname"]}'
engine = create_engine(conn_str)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Weather(Base):
    __tablename__ = 'weather'
    row_id = Column(BigInteger, primary_key=True)
    title = Column(String, nullable=False)
    woeid = Column(Integer, nullable=False)
    id = Column(String, nullable=False)
    weather_state_name = Column(String, nullable=False)
    weather_state_abbr = Column(String, nullable=False)
    wind_direction_compass = Column(String, nullable=False)
    created = Column(String, nullable=False)
    applicable_date = Column(Date, nullable=False)
    min_temp = Column(Numeric, nullable=False)
    max_temp = Column(Numeric, nullable=False)
    the_temp = Column(Numeric, nullable=False)
    wind_speed = Column(String, nullable=False)
    wind_direction = Column(String, nullable=False)
    air_pressure = Column(Numeric, nullable=False)
    humidity = Column(Integer, nullable=False)
    visibility = Column(String, nullable=False)
    predictability = Column(Integer, nullable=False)
