from collections import ChainMap
import json
from os.path import exists
import asyncio
from typing import List, Dict
import aiohttp
import aiofiles


def read_input_file(file_name: str) -> List[str]:
    """
    Reads the input file and returns a list of cities.
    """
    with open(file_name, 'r') as f:
        cities = json.load(f)
        cities = cities["cities"]
    return cities


async def get_woeid(city: str) -> Dict[str, str]:
    """
    Gets the WOEID of a city.
    """
    url = f"https://www.metaweather.com/api/location/search/?query={city}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            woeid = data[0]["woeid"]
            result = {city: woeid}
    return result


async def get_weather(woeid: int) -> Dict:
    """
    Get weather data from MetaWeather.com API with woeid
    :param woeid: woeid of the city or location
    """
    url = f'https://www.metaweather.com/api/location/{woeid}/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def get_weather_multiple(woeids: Dict[str, str]) -> List[Dict]:
    """
    Gather coroutines to get weather data for multiple cities
    :param woeids: list of woeids
    """
    tasks = [get_weather(woeid) for city, woeid in woeids.items()]
    return await asyncio.gather(*tasks)


async def write_to_csv(filename: str, data: List[Dict]) -> None:
    """
    Write weather data to csv file
    :param filename: output filename
    :param data: weather data
    """
    if not exists(filename):
        async with aiofiles.open(filename, 'w') as f:
            header = data[0]
            header = ['title', 'woeid'] + [key for key in header['consolidated_weather'][0].keys()]
            await f.write(','.join(header) + '\n')
    async with aiofiles.open(filename, 'a') as f:
        for row in data:
            title = str(row['title'])
            woeid = str(row['woeid'])
            consolidated_weather = ','.join([str(x) for x in row['consolidated_weather'][0].values()])
            row_processed = ','.join([title, woeid, consolidated_weather, '\n'])
            await f.write(row_processed)


async def main():
    cities = read_input_file("cities.json")
    tasks = [get_woeid(city) for city in cities]
    woeids = await asyncio.gather(*tasks)
    woeids = dict(ChainMap(*woeids))
    weather_data = await get_weather_multiple(woeids)
    await write_to_csv('weather.csv', weather_data)

if __name__ == '__main__':
    asyncio.run(main())
