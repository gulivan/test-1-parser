from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from database import engine, Weather

app = FastAPI()

@app.get("/")
async def root():
    html_content = '''<a href="/api/weather/city=Madrid">Try to get the last weather data from Madrid</a>
    or checkout the <a href="/docs">swagger interactive documentation</href>'''
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/api/weather/show_locations")
async def get_locations_and_woeids():
    """
    Returns a list of locations and woeids
    """
    session = Session(bind=engine, expire_on_commit=False)
    weather = session.query(Weather).with_entities(Weather.woeid, Weather.title).distinct()
    session.close()
    return weather


@app.get("/api/weather/city={title}")
async def get_weather_by_city_title(title: str, limit: int = 1):
    """
    Returns the N weather data from a city. N - is a number defined by limit.
    :param title: City title
    :param limit: Limit
    :return:
    """
    session = Session(bind=engine, expire_on_commit=False)
    weather = session.query(Weather).filter(Weather.title == title).order_by(Weather.created.desc()).limit(limit).all()
    session.close()
    return weather


@app.get("/api/weather/woeid={woeid}")
async def get_weather_by_woeid(woeid: str, limit: int = 1):
    """
    Returns the N weather data from a woeid. N - is a number defined by limit.
    :param woeid: Location woeid
    :param limit: Limit
    :return:
    """
    session = Session(bind=engine, expire_on_commit=False)
    weather = session.query(Weather).filter(Weather.woeid == woeid).order_by(Weather.created.desc()).limit(limit).all()
    session.close()
    return weather
