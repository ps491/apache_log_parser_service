import asyncio
from datetime import datetime
import requests
TIME_INTERVAL_IN_SEC = 15


async def crawl_websites():
    while True:
        # async GET requests
        print("куку")
        print(requests.get('http://127.0.0.1:8000/api/worker/order/close/'))
        print(datetime.utcnow())
        # async update DB
        await asyncio.sleep(TIME_INTERVAL_IN_SEC)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task = loop.create_task(crawl_websites())
    loop.run_until_complete(task)
