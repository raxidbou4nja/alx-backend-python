#!/usr/bin/env python3
""" 1. Async Comprehensions """
import asyncio
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        async_comprehension that takes no arguments
    """
    async_numbers = [num async for num in async_generator()]
    return async_numbers
