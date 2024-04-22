#!/usr/bin/env python3
""" multiple coroutines  """
import asyncio
from typing import List
from random_async import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that spawns n instances of
    wait_random coroutine with the specified max_delay
    and returns the list of delays in ascending order.
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
