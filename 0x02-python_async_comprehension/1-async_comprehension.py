#!/usr/bin/env python3
""" 1. Async Comprehensions """
import asyncio
import random


async def async_generator():
    """
        async_generator that takes no arguments
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension():
    """
        async_comprehension that takes no arguments
    """
    async_numbers = [num async for num in async_generator()]
    return async_numbers
