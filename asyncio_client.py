import asyncio
import time
import aiohttp
import motor.motor_asyncio

mongo_uri = 'mongodb://127.0.0.1:27017'
motor_client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
db = motor_client['test']
collection = db['testing']


async def download_site(session, url):
    async with session.get(url) as response:
        text = await response.text()
        result = await collection.insert_one({text: text})
        print('result %s' % repr(result.inserted_id))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
                "http://localhost:5000",
            ] * 150000
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")
