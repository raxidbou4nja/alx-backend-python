#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import asyncio
import random
import time


async def async_generator():
    """
        async_generator function: without args
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension():
    """
        async_comprehension function: without args
    """
    async_numbers = [num async for num in async_generator()]
    return async_numbers


async def measure_runtime():
    """
        measure_runtime function: without args
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension(),
                async_comprehension(),
                async_comprehension(),
                async_comprehension())
    end_time = time.time()
    return end_time - start_time
