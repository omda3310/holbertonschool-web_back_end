#!/usr/bin/env python3
"""
an asynchronous coroutine that takes in an integer argument
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Return a random delay between 0 and max_delay"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
