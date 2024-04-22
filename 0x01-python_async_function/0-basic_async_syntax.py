#!/usr/bin/env python3
""" The basics of async  """

import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay
    (inclusive) seconds and eventually returns it.
    Args: max_delay (int): The maximum delay allowed (default is 10).
    Returns: float: The random delay waited.
    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
